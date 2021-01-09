import re
import requests
from bs4 import BeautifulSoup


BASE_URL = 'https://en.uesp.net'
BOOK_LIST_URL = '/wiki/Skyrim:Books'

r = requests.get(f'{BASE_URL}{BOOK_LIST_URL}')
html = r.text
soup = BeautifulSoup(html, 'html.parser')

table = soup.find('table', {'class': 'wikitable sortable collapsible striped'})
rows = table.find_all('tr')

books = []

# scrape the HTML table for data about the books
for tr in rows[1:]: # skip over first entry which is an empty list
    td = tr.find_all('td')
    row = [i.text for i in td]

    book_url = td[1].find('a')['href']
    row.append(f'{BASE_URL}{book_url}') # index 1 contains the url for the book
    
    row = row[1:] # exclude the first index that always contains '\n\n'
    
    row[0] = row[0][:row[0].index('\n')] # trim off nonsense at the end of the title

    row[1] = re.search('[0-9]+', row[1]).group() # some values contain text, this extracts the number

    row = [data.replace('\n', '') for data in row]

    books.append(row)

# save the data to a csv
# using pipe as a delimiter since some fields have commas
with open('books.csv', 'w') as f:
    f.write('Title|Value|Author|Description|Type|URL\n')
    for book in books:
        for i, data in enumerate(book):
            f.write(data)
            if i < len(book) - 1:
                f.write('|')
        
        f.write('\n')

    f.close()
