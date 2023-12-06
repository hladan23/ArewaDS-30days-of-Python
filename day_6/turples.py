# Exercise: Level 1
empty_tupple = ()

sisters = ('Jamila', 'Aisha', 'Hadiza')
brothers = ('Ahmad', 'Abdullah', 'Ibrahim')

siblings = brothers + sisters 

print(len(siblings))

family_members = siblings + ('Umar', 'Lubnah')
print(family_members)

# Exercise: Level 2
*siblings, father, mother = family_members
print(siblings)
print(father, mother)

fruits = ('Apple', 'melon', 'pineapple', 'guava', 'cherry')
vegetables = ('peas', 'carrot', 'lettuce')
animal_product = ('meat', 'sausage', 'fish')

food_stuff_tp = fruits + vegetables + animal_product
print(food_stuff_tp)

food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

print(len(food_stuff_lt))
print(food_stuff_lt[5:7])

print(food_stuff_lt[:3])

del food_stuff_tp

nordic_countries = ('Finland','Denmark', 'Iceland', 'Norway', 'Ireland', 'Sweden')

print('Estonia' in nordic_countries)

print('Iceland' in nordic_countries)