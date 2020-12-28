# This will get the book data and URL from books.csv and store it in SkyrimLibrary.db

import requests
import pandas as pd
from bs4 import BeautifulSoup
import sqlite3

conn = sqlite3.connect('SkyrimLibrary.db')
cursor = conn.cursor()

df = pd.read_csv('DataCollection/books.csv', delimiter='|')

df = df.where(pd.notnull(df), '') # replace nan with empty string

# scrape book text and insert book info into Book table
for i in range(len(df)):
    r = requests.get(df.iloc[i]['URL'])
    html = r.text
    soup = BeautifulSoup(html, 'html.parser')

    # need to fix this later, some books' content aren't in a div with class "book"
    # skipping over these for now
    try:
        # Some books start with a fancy letter that is actually an image.
        # Need to find a way to get that letter as well so the first letter of the
        # book isn't cut off.
        book_content = soup.find('div', {'class': 'book'}).text

        cursor.execute("""
            INSERT INTO Book(Title, Value, Author, Description, Type, Content)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            [
                df.iloc[i]['Title'],
                int(df.iloc[i]['Value']), # can't use numpy data types
                df.iloc[i]['Author'],
                df.iloc[i]['Description'],
                df.iloc[i]['Type'],
                book_content
            ]
        )

    except:
        pass

conn.commit()
conn.close()
