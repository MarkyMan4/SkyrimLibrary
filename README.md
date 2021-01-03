# SkyrimLibrary
Scraping the text from books in Skyrim and storing them in a database, doing analysis and exposing a REST API.


## Each folder should have it's own virtual environment since they serve different purposes

### DataCollection
Run scripts in this order: 
1. db_setup.py
2. get_book_urls.py
3. save_to_db.py

Then the notebooks can be run.

### BookAPI
Inside this folder, run <code>uvicorn main:app</code> to start the server.

