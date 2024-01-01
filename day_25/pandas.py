# Exercises: Day 25

# Q1
import pandas as pd 
import numpy  as np 

df = pd.read_csv('ArewaDS-30days-Of-Python\day_25\hacker_news.csv')
print(df)

# Q2
first_five_rows = df.head()
print(first_five_rows)

# Q3
last_five_rows = df.tail()
print(last_five_rows)

# Q4
title_series = df['title']
print(title_series)

# Q5
num_rows, num_columns = df.shape
print(f"Number of rows: {num_rows}") 
print(f"Number of columns: {num_columns}") 

# Filter Titles Containing 'Python'
python_titles = df[df['title'].str.contains('Python', case=False)]
print(python_titles) # [160 rows x 7 columns]

# Filter Titles Containing 'JavaScript'
js_titles = df[df['title'].str.contains('JavaScript', case=False)]
print(js_titles) # [170 rows x 7 columns]

# Explore the data and make sense of it
df.info() # the dataframe information are  data types, columns, rangeIndex
df.describe() # the descriptive statistics of the dataframe are count, mean, std, min, max









