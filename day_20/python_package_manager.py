# Exercises: Day 20
# Q1.

import requests
from collections import Counter
import re

# URL of the text
url = 'http://www.gutenberg.org/files/1112/1112.txt'

# Fetching the text from the URL
response = requests.get(url)
text = response.text

# Clean and preprocess the text
cleaned_text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
words = cleaned_text.lower().split()  # Convert to lowercase and split into words

# Count occurrences of each word
word_counts = Counter(words)

# Find the top 10 most frequent words
top_10_words = word_counts.most_common(10)
print(top_10_words)


# Q2.

cats_api = 'https://api.thecatapi.com/v1/breeds'

response = requests.get(cats_api)

if response.status_code == 200:
    cat_breeds = response.json()
else:
    print("Failed to retrieve information from API")

'''getting the list of the weights of all the cats in metric units, 
has upper and lower limits'''
cat_weight_metric = []
for i in range(len(cat_breeds)):
  cat_weight_metric.append(cat_breeds[i]['weight']['metric'])
cat_weight_metric[:5]

# for lifespan
cat_weight_lifespan = []
for i in range(len(cat_breeds)):
  cat_weight_lifespan.append(cat_breeds[i]['life_span'])
cat_weight_lifespan[:5]

# getting a function to make them integers and get two lists of upper and lower limits
def convert_to_numbers(string):
    start, end = map(int, string.split(" - "))
    return start, end

# converting the weights to numbers using the function to get upper and lower weight limits for each, two lists:
cat_weight_metric_number = list(map(convert_to_numbers,cat_weight_metric))
lower_cat_weight_metric,upper_cat_weight_metric = [i[0] for i in cat_weight_metric_number],[i[1]for i in cat_weight_metric_number]

# lifespans in years
cat_lifespan_number = list(map(convert_to_numbers,cat_weight_lifespan))
lower_cat_lifespan,upper_cat_lifespan = [i[0] for i in cat_lifespan_number],[i[1]for i in cat_lifespan_number]

# Using descriptive statistics (mean,median and std) 
# for the lower and upper limits, using the min and max list methods
import statistics as stats
print(f'Max of upper limit of cat\'s weights in metric units is: {max(upper_cat_weight_metric)} ')
print(f'Min of upper limit of cat\'s weights in metric units is: {min(upper_cat_weight_metric)} ')
print(f'Mean of upper limit of cat\'s weights in metric units is: {stats.mean(upper_cat_weight_metric)} ')
print(f'Median of upper limit of cat\'s weights in metric units is: {stats.median(upper_cat_weight_metric)} ')
print(f'Std of upper limit of cat\'s weights in metric units is: {stats.stdev(upper_cat_weight_metric)} ')

# using the function below to get the parameters
def stats_params(list):
    '''
    Takes a list and returns a dictionary of certain statistics parameters of the list
    '''
    import statistics as stats
    stat = {}
    stat['Max'] = max(list)
    stat['Minimum'] = min(list)
    stat['Mean'] = stats.mean(list)
    stat['Median'] = stats.median(list)
    stat['std'] = stats.stdev(list)
    return stat
print(stats_params(upper_cat_weight_metric))



print(f'Upper limit of cat weights in metric units: {stats_params(upper_cat_weight_metric)}, lower limit of cat weights in metric units: {stats_params(lower_cat_weight_metric)},upper limit of cat lifespan in years : {stats_params(upper_cat_lifespan)},lower limits of cat lifespan in years: {stats_params(lower_cat_lifespan)}')
answer_dict = {}
answer_dict['Upper limit stats of cat weights in metric units'] = stats_params(upper_cat_weight_metric)
answer_dict['Lower limit stats of cat weights in metric units'] = stats_params(lower_cat_weight_metric)
answer_dict['Upper limit stat of cat lifespan in years'] = stats_params(upper_cat_lifespan)
answer_dict['Lower limit stats of cat lifespan in years'] = stats_params(lower_cat_lifespan)
print(f'Answer to first two sub questions of question 2: {answer_dict}')


from collections import defaultdict
# Getting the frequency table 
frequency_table = defaultdict(int)
breed_info = {}
for breed in cat_breeds:
    breed_info[breed['name']] = breed['origin']
for breed in breed_info.values():
    frequency_table[breed] += 1

print(frequency_table)

# Q3.

import requests
from bs4 import BeautifulSoup

url = 'https://archive.ics.uci.edu/ml/datasets.php'

# Sending a GET request to the URL and retrieve the HTML content
response = requests.get(url)
html_content = response.content

# Parse the HTML content using BeautifulSoup4
soup = BeautifulSoup(html_content, 'html.parser')

# Finding the table that contains the list of data sets
table = soup.find('table', {'border': '1'})
# Q4
# Extracting the name of each data set from the table rows, for now, a humble goal due to my current limited skills
rows = table.find_all('tr')[1:]
for row in rows:
    cells = row.find_all('td')
    name = cells[0].text.strip()
    # Gives the names of all the datasets in the table
    print(f'{name}')