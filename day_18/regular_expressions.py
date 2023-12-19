# Exercise: Level 1

import re
# Q1.
from collections import Counter

paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

# Tokenize the paragraph into words
words = paragraph.split()

# Counting the frequency of each word
word_counts = Counter(words)

# Finding the most common word
most_common_word, frequency = word_counts.most_common(1)[0]

print(f"The most frequent word is '{most_common_word}' with a frequency of {frequency}.")

# Q2
import re

text = "The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction."

# Extracting numbers from the text using regular expression
points = [int(match.group()) for match in re.finditer(r'-?\d+', text)]

# Sorting the list of points
sorted_points = sorted(points)

# Finding the distance between the two furthest points
if len(sorted_points) >= 2:
    distance = sorted_points[-1] - sorted_points[0]
    print(f"The distance between the two furthest particles is {distance}.")
else:
    print("Insufficient number of points.")
    
# Exercises: Level 2
# Q1.

import re

def is_valid_variable(variable):
    pattern = re.compile(r'^[a-zA-Z_][a-zA-Z0-9_]*$')
    return bool(pattern.match(variable))
# outputs
print(is_valid_variable('first_name'))   # True
print(is_valid_variable('first-name'))   # False
print(is_valid_variable('1first_name'))  # False
print(is_valid_variable('firstname'))    # True

# Exercises: Level 3
import re
from collections import Counter

def clean_text(text):
    # Removing special characters and extra spaces
    cleaned_text = re.sub(r'[^a-zA-Z\s]', '', text)

    # Removing extra spaces and convert to lowercase
    cleaned_text = ' '.join(cleaned_text.split()).lower()

    return cleaned_text

def most_frequent_words(text, n=3):
    words = text.split()
    word_counts = Counter(words)
    return word_counts.most_common(n)

# Given sentence
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

# Clean the text
cleaned_text = clean_text(sentence)

# Output cleaned text
print(cleaned_text)

# Find the three most frequent words
result = most_frequent_words(cleaned_text, n=3)
print(result)


        
