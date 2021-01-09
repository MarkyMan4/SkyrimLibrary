# set up script to create a virtual environment, install dependencies,
# create the database, and insert all the data
python -m venv venv
. venv/bin/activate

pip install -r requirements.txt

python db_setup.py
python get_book_urls.py
python save_to_db.py
