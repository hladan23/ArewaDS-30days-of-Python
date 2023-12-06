# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Exercise: Level 1
print(len(it_companies))

it_companies.add('Twitter')
print(it_companies)

it_companies.update(['NITDA', 'Cisco', 'Oracle'])
print(it_companies)

it_companies.remove('Oracle')
print(it_companies)

# Question 5. What is the difference between remove and discard?
## Answer:- when the item of a given set is not found, the remove() function will raise errors, while the discard () function doesn't raise any errors.

# Excercise: Level 2
C = A.union(B)
print(C)

print(A.intersection(B))

print(A.issubset(B))

print(A.isdisjoint(B))

print(A.union(B) & B.union(A))

A.symmetric_difference(B)

del A, B

# Excercise: Level 3
ages = set(age)
print(ages)
print(len(age) > len(ages))

# The differences between the string, list, tuple, and set are:

# String: A string is a sequence of characters. It is a data type used to represent text and is typically enclosed in single or double quotes. 
# Strings are immutable, meaning that their contents cannot be changed after they are created. Operations on strings create new strings.

# List: A list is an ordered collection of items. It can contain elements of different data types, and it is defined using square brackets [].
# Lists are mutable, meaning you can modify their elements by assigning new values or using methods like append, remove, etc.

# Tuple: A tuple is similar to a list, but it is immutable. Tuples are defined using parentheses ().
# Tuples are immutable, so once they are created, their elements cannot be changed.

# Set: A set is an unordered collection of unique elements. It is defined using curly braces {} or the set() constructor.
# Sets are mutable; you can add and remove elements, but the elements themselves are immutable.

# I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words. 

sentence = 'I am a teacher and I love to inspire and teach people'
sentence = sentence.split(' ')

print(sentence)
print(sentence[8], ' and ', sentence[10])

