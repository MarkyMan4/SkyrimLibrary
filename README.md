# SkyrimLibrary
Scraping the text from books in Skyrim and storing them in a database, doing analysis and exposing a REST API.


## Each folder has it's own virtual environment since they serve different purposes

### DataCollection
In the DataCollection directory, run setup.sh. <br>
This will create a virtual environment, install dependencies from requirements.txt, and create
the database in the correct directory and run the scripts to populate it with data. 
Takes a few minutes to run.

The scripts are run in this order: 
1. db_setup.py
2. get_book_urls.py
3. save_to_db.py

Then the notebooks can be used.

### BookAPI
Inside this folder, run <code>uvicorn main:app</code> to start the server.

