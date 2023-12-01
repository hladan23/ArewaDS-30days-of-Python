list =  []

fruits = ['banana', 'orange', 'mango','berries', 'lemon', 'melon', 'pawpaw']

print(len(fruits))

first_fruit, a, b, middle_fruit, c, d, last_fruit, = fruits 
print(first_fruit)     # banana
print(middle_fruit)    # berries
print(last_fruit)      # pawpaw

mixed_data_types = ["hajara", 30, 45, 'single', 'kaduna']

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

print(mixed_data_types)
print(it_companies)

print(len(it_companies))

a,b,c,d,e,f,g = it_companies
print(a)
print(d)
print(g)

it_companies[0] = "META"
print(it_companies)

it_companies.append('Kaggle')
print(it_companies)

it_companies.insert( 3, 'Digital Ocean')
print(it_companies)

it_companies[4] = it_companies[4].upper()
print(it_companies)

result = '#; '.join(it_companies)
print(result)

print(it_companies.index('Microsoft'))

it_companies.sort()
print(it_companies)

it_companies.reverse()
print(it_companies)