# Exercises: Day 22
# Q1 Scrape the following website and store the data as json file(url = 'http://www.bu.edu/president/boston-university-facts-stats/').

import requests
from bs4 import BeautifulSoup
import json


url = 'http://www.bu.edu/president/boston-university-facts-stats/'
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, 'lxml')

# Define data structure for scraped information
data = {
    'quick_facts': {},
    'community': {},
}

# Extract quick facts
quick_facts_table = soup.find('table', class_='table table-stripped')
for row in quick_facts_table.find_all('tr'):
    key, value = row.find_all('td')
    data['quick_facts'][key.text.strip()] = value.text.strip()

# Extract community info
community_table = soup.find('table', class_='table table-striped table-condensed')
for row in community_table.find_all('tr'):
    key, value = row.find_all('td')
    data['community'][key.text.strip()] = value.text.strip()

# Save data as JSON
with open('bu_facts_stats.json', 'w') as f:
    json.dump(data, f, indent=4)

print('Data scraped and saved to bu_facts_stats.json')

# Q2 Extract the table in this url (https://archive.ics.uci.edu/ml/datasets.php) and change it to a json file

url = 'https://archive.ics.uci.edu/ml/datasets.php'

response = requests.get(url)
content = response.content # we get all the content from the website
soup = BeautifulSoup(content, 'html.parser') # beautiful soup will give a chance to parse
print(soup.title) # <title>UCI Machine Learning Repository: Data Sets</title>
print(soup.title.get_text()) # UCI Machine Learning Repository: Data Sets
print(soup.body) # gives the whole page on the website
print(response.status_code)

tables = soup.find_all('table', {'cellpadding':'3'})
# We are targeting the table with cellpadding attribute with the value of 3
# We can select using id, class or HTML tag , for more information check the beautifulsoup doc
table = tables[0]
with open('dataset_table.json','w') as f:
    json.dump(table,f)

# Q3 Scrape the presidents table and store the data as json(https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States). The table is not very structured and the scrapping may take very long time.
# Send an HTTP request to the Wikipedia page
url = 'https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States'
response = requests.get(url)

# Parse the HTML code using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the presidents table and extract the data
table = soup.find('table', {'class': 'wikitable sortable'})
headers = [header.text.strip() for header in table.find_all('th')]
rows = []
for row in table.find_all('tr')[1:]:
    cells = [cell.text.strip() for cell in row.find_all('td')]
    rows.append(dict(zip(headers, cells)))

# Store the data as JSON
with open('presidents.json', 'w') as f:
    json.dump(rows, f)