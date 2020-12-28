# This will get the book data and URL from books.csv and store it in SkyrimLibrary.db

import requests
import pandas as pd
from bs4 import BeautifulSoup

df = pd.read_csv('DataCollection/books.csv', delimiter='|')
print(df)
