import random
import requests
import json
import re

""" Config data """

# Enter your integration token here
INTEGRATION_TOKEN = ""
# Enter your database id here
NOTION_DATABASE_ID = ""
# Enter the number of pages you want to randomly retrieve
num_random_pages = 3
# Enter here the name of the checkbox property
prop_name = ""


""" Functions. Do not change anything here unless you want to modify how the program works """


def queryDatabase(database_id, token):
    # Because the limit of pages one can query per request is 100 we loop through the database and make multiple querries to get all pages.
    has_more = None
    next_cursor = None
    url = f"https://api.notion.com/v1/databases/{database_id}/query"

    while (has_more == None or has_more == True):
        # If there is no "next_curser" (e.g. it's the first or only query) make a default request
        if (next_cursor == None):
            db = getDatabaseSection(url, token)

        # If there is a "next_cursor" use it as "start_cursor" for the next request
        else:
            db_section = getDatabaseSection(url, token, next_cursor)
            db["results"].extend(db_section["results"])
            db["has_more"] = db_section["has_more"]
            db["next_cursor"] = db_section["next_cursor"]

        # Update iteration variables
        has_more = db["has_more"]
        if (has_more):
            next_cursor = db["next_cursor"]

    # Return data for use in future steps
    return db


def getDatabaseSection(url, token, next_cursor=None):
    if (next_cursor):
        payload = {
            "page_size": 100,
            "start_cursor": next_cursor
        }
    else:
        payload = {
            "page_size": 100,
        }
    headers = {
        "Authorization": f"Bearer {token}",
        "accept": "application/json",
        "Notion-Version": "2022-06-28",
        "content-type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    return response.json()


def updatePages(token, db, num_random_pages):
    # Uncheck old pages.
    for page in db["results"]:
        if (page["properties"][prop_name]["checkbox"] == True):
            updatePage(token, page["id"], False)

    # Check new pages
    n = len(db["results"])
    randIndices = random.sample(range(n), num_random_pages)

    for index in randIndices:
        id = db["results"][index]["id"]
        updatePage(token, id, True)


def updatePage(token, page_id, value):
    url = f"https://api.notion.com/v1/pages/{page_id}"
    payload = {
        "properties": {
            prop_name: {
                "id": "~ePN",
                "type": "checkbox",
                "checkbox": value
            }
        }
    }

    headers = {
        "Authorization": f"Bearer {token}",
        "accept": "application/json",
        "Notion-Version": "2022-06-28",
        "content-type": "application/json"
    }
    response = requests.patch(url, json=payload, headers=headers)


def validate_token(token):
    # Return false if that the token is not of the expected format
    pattern = r"^secret_[a-zA-Z0-9]{43}$"
    if not re.match(pattern, token):
        return False
    return True


def validate_database_id(database_id):
    # Return false if that the database id is not of the expected format
    pattern = r"^[a-zA-Z0-9]{32}$"
    if not re.match(pattern, database_id):
        return False
    return True


'''The main program'''

# Validate the config data
if not validate_token(INTEGRATION_TOKEN):
    raise ValueError("Invalid token")
if not validate_database_id(NOTION_DATABASE_ID):
    raise ValueError("Invalid database id")
if not (isinstance(num_random_pages, int) and 0 < num_random_pages <= 100):
    raise ValueError(
        "Invalid number of pages to update. Please enter a number between 1 and 100.")

# Get data from the database and update its pages
database = queryDatabase(NOTION_DATABASE_ID, INTEGRATION_TOKEN)
updatePages(INTEGRATION_TOKEN, database, num_random_pages)
