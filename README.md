# Notion Random Note Generator #
This integration allows you to randomly resurface old ideas from your Notion database (of any size), helping you to review them and understand them in a new way. It's inspired by the concept of serendipity from the book "Where Good Ideas Come from: The Natural History of Innovation" by Steven Johnson.

## Motivation ##
When you capture your ideas, notes, quotes, and resources in a hierarchical database like Notion, it's easy to get stuck in the same patterns of thinking and miss out on serendipitous connections between ideas. The ability to filter content further narrows your perspective and limits your creative output. The purpose of this script is to randomly bring back serendipity to your note taking system by resurfacing old ideas from your database and providing you with an opportunity to review them with fresh eyes.

## How to Use ##
1. **Set up your Notion database**: Add a checkbox property called "Today's idea" to your database. This propterty will be used to mark the randomly selected pages.

2. **Create a Notion Integration**: Go to the Notion Developer page (https://developers.notion.com) and create a new integration following the instructions on the website. Make sure you grant it access to the database you want to connect to.

3. **Create a Pipedream workflow**: Sign up for a Pipedream account and create a new workflow following the instructions on the Pipedream website (https://pipedream.com). Set the workflow to execute at your preferred time (e.g. 5 AM every day) or choose any trigger of your liking.

4. **Copy-paste the code**: When you set up your Pipedream workflow, copy-paste the code from the app.py file into the code box.

5. **Enter the necessary information**: Fill in the integration token, the database ID, and the number of pages you want to randomly retrieve. This information should be included at the top of the script.

6. **Retrieve pages**: In Notion, create a new database view with a filter for "Today's idea: checked" or just use a sort to make the marked pages appear at the top of your current database view.

7. **Customization**: You can customize the code as you like e.g. change the property name of "Today's idea" to something else, just make sure you change the property name everywhere in the code as well or the script won't work as desired.

That's it! With these simple steps, you'll be on your way to rediscovering old ideas and finding new inspiration in your Notion database.
