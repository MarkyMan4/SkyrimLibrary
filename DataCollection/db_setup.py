# Run this script prior to collecting data to get the database created.
# This also creates a table called Book where the data will be stored.

import sqlite3

conn = sqlite3.connect('../SkyrimLibrary.db')
cursor = conn.cursor()

# Create the Book table
cursor.execute('''
CREATE TABLE Book (
    ID          INTEGER         PRIMARY KEY ASC AUTOINCREMENT,
    Title       VARCHAR (100)   NOT NULL,
    Value       INTEGER,
    Author      VARCHAR (50),
    Description VARCHAR(100),
    Type        VARCHAR (100),
    Content     VARCHAR (10000) NOT NULL
)
''')

conn.commit()
