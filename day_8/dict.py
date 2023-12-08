# Empty dictionary 
dog = {}
# adding keys to empty dictionary
dog = {'name': 'bingo', 'color': 'chocolate', 'breed': 'German_Shepherd', 'legs': 'brown', 'age': 5}
# student dictionary
student = {'first_name': 'Hajara', 'last_name': 'Ladan', 'gender': 'female', 'age': 38, 'marital_status': 'married', 'skills':['painter'], 'country': 'Nigeria', 'city': 'Kaduna', 'address': 'Zaria'}
# length of student dictionary
print(len(student))
# value of skills
skills = student['skills']
print(skills)
# modifying skills
student['skills'].append('capentary')
print(student)
# dictionary keys as a list
print(student.keys()) 
# dictionary values as a list
print(student.values())
# changing dictionary to list of tuples
print(student.items())
# deleting one of the items 
student.pop('skills')
print(student)
# deleting one of the dictionaries
del dog
