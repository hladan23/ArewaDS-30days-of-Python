# Exercises: Level 1

# import required libraries
import re, json, csv

# Q1 Write a function which count number of lines and number of words in a text.
# All the files are in the data folder: a) Read obama_speech.txt file and count number of lines and words 
# b) Read michelle_obama_speech.txt file and count number of lines and words 
# c) Read donald_speech.txt file and count number of lines and words 
# d) Read melania_trump_speech.txt file and count number of lines and words

def count_lines_words(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            num_lines = len(lines)
            words = ' '.join(lines).split()
            num_words = len(words)
            
            print(f"File: {file_path}")
            print(f"Number of lines: {num_lines}")
            print(f"Number of words: {num_words}")
            print("-" * 30)
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")

# File paths
file_paths = [
    r'C:\Users\Aisha\projects\ArewaDS-30days-Of-Python\day_19\melania_trump_speech.txt',
    r'C:\Users\Aisha\projects\ArewaDS-30days-Of-Python\day_19\michelle_obama_speech.txt',
    r'C:\Users\Aisha\projects\ArewaDS-30days-Of-Python\day_19\obama_speech.txt',
    r'C:\Users\Aisha\projects\ArewaDS-30days-Of-Python\day_19\donald_speech.txt'
]

# Count lines and words for each file
for file_path in file_paths:
    count_lines_words(file_path)

# Q2 
# Q3
import json

def most_spoken_languages(filename, top_n):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)

    languages_count = {}
    for country_info in data:
        languages = country_info.get('languages', [])
        for language in languages:
            languages_count[language] = languages_count.get(language, 0) + 1

    sorted_languages = sorted(languages_count.items(), key=lambda x: x[1], reverse=True)
    return sorted_languages[:top_n]

file_path = 'ArewaDS-30days-Of-Python\day_19\countries_data.json'

# Get the 10 most spoken languages
top_10_languages = most_spoken_languages(filename=file_path, top_n=10)
print(top_10_languages) 

# Get the 3 most spoken languages
top_3_languages = most_spoken_languages(filename=file_path, top_n=3)
print(top_3_languages)

# Exercise Level 2
# Extract all incoming email addresses as a list from the email_exchange_big.txt file.
with open('ArewaDS-30days-Of-Python\day_19\email_exchange_big.txt') as f:
    lines = f.readlines()
email_addresses = []
for line in lines:
    #using regex to get alphanumeric characters before and after and @ symbol. \S is non-whitespace characters
    email_addresses.extend(re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]', line))
email_addresses[:]

# Q5 Find the most common words in the English language. Call the name of your function find_most_common_words, it will take two parameters - a string or a file and a positive integer, indicating the number of words. Your function will return an array of tuples in descending order. Check the output
    
def find_most_common_words(file,n=10):
    
    # Returns a list of tuples showing the count of the n most common words in the document, file
    
    with open(file) as f:
        lines = f.readlines()
    words = []
    for line in lines:
        # removing all characters that are not whitespace or alphanumeric using regex
        line = re.sub(r'[^\w\s]','',line)
        words.extend(line.split())
    words_dict = {}
    for word in words:
        words_dict[word] = words_dict.get(word,0) + 1
    words_sorted = sorted(words_dict.items(),key=lambda x:x[1],reverse=True)
    result = [(word[1],word[0]) for word in words_sorted]
    return result[:n]

# Q6 Use the function, find_most_frequent_words to find: 
# a) The ten most frequent words used in Obama's speech 
print(find_most_common_words('ArewaDS-30days-Of-Python\day_19\obama_speech.txt'))

# b) The ten most frequent words used in Michelle's speech 
print(find_most_common_words('ArewaDS-30days-Of-Python\day_19\michelle_obama_speech.txt'))

# c) The ten most frequent words used in Trump's speech 
print(find_most_common_words('ArewaDS-30days-Of-Python\day_19\donald_speech.txt'))

# d) The ten most frequent words used in Melina's speech
print(find_most_common_words('ArewaDS-30days-Of-Python\day_19\melania_trump_speech.txt'))


# Q7 Write a python application that checks similarity between two texts. 
# It takes a file or a string as a parameter and it will evaluate the similarity of the two texts. 
# For instance check the similarity between the transcripts of Michelle's and Melina's speech. You may need a couple of functions, function to clean the text(clean_text), function to remove support words(remove_support_words) and finally to check the similarity(check_text_similarity).
# List of stop words are in the data directory

def clean_text(file):
    '''
    Returns all the words in a text after removing the punctuations and others
    '''
    with open(file) as f:
        lines = f.readlines()
        words = []
        for line in lines:
            # removing all characters that are not whitespace or alphanumeric using regex
            line = re.sub(r'[^\w\s]','',line)
            words.extend(line.split())
    return words


clean_text('ArewaDS-30days-Of-Python\day_19\michelle_obama_speech.txt')

# onto removing stop words

from stop_words import stop_words
def remove_stop_words(list):
    '''Removes stop words, i.e. commonly used words that search engines are programmed to ignore, from a list of words'''
    return [word for word in list if word.lower() not in stop_words]
remove_stop_words(clean_text('ArewaDS-30days-Of-Python\day_19\michelle_obama_speech.txt')) 

# next, function for similarity
def check_text_similarity(list_one,list_two):
    '''Gives a percentage of similar words in two different lists'''
    res = [x for x in (list_one + list_two) if x in list_one and x in list_two]
    similar_words_percent = (len(res)/(len(list_one) + len(list_two))) * 100
    return similar_words_percent
check_text_similarity(['apple','banana','mango','pawpaw'],['apple','mango','pear']) # worked.


# combining the functions 
def comparing_text_in_file_similarity(file_one,file_two):
    '''Gives the percentage of similar words in two different files'''
    file_one_words = remove_stop_words(clean_text(file_one))
    file_two_words = remove_stop_words(clean_text(file_two))
    return check_text_similarity(file_one_words,file_two_words)

comparing_text_in_file_similarity('ArewaDS-30days-Of-Python\day_19\michelle_obama_speech.txt','ArewaDS-30days-Of-Python\day_19\melania_trump_speech.txt') # Got 43.44% similarity. 

#Q8 Find the 10 most repeated words in the romeo_and_juliet.txt

print(find_most_common_words('ArewaDS-30days-Of-Python\day_19\romeo_and_juliet.txt'))


# Q9 Read the hacker news csv file and find out:
# a) Count the number of lines containing python or Python 
# b) Count the number lines containing JavaScript, javascript or Javascript
# c) Count the number lines containing Java and not JavaScript'''

with open('ArewaDS-30days-Of-Python\day_19\hacker_news.csv',newline='') as f:
    csv_reader = csv.reader(f,delimiter=',')
    python_rows = 0
    javascript_rows = 0
    java_rows = 0
    for row in csv_reader:
        for i in range(len(row)):
            if re.findall(r'[Pp]ython',row[i]):
                python_rows += 1
            elif re.findall(r'[Jj]ava[Ss]cript',row[i]):
                javascript_rows +=1
            elif re.findall(r'Java$',row[i]):
                java_rows +=1
print(f'the number of lines containing a,b and c respectively are: {python_rows}, {javascript_rows} and {java_rows}')
# the number of lines containing a,b and c respectively are: 266, 238 and 7