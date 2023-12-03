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

print(it_companies[0:3])

print(it_companies[-1:-4:-1])

print(it_companies[4:5])

del it_companies[0]
print(it_companies)

del it_companies[4]
print(it_companies)
 
del it_companies[-1]
print(it_companies)
 
del it_companies[0:]
print(it_companies)
 
del it_companies

# Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
program = front_end + back_end
 
full_stack = program.copy()
print(full_stack)
 
new=['Python','SQL']
full_stack.insert(5, new)
print(full_stack)

# Exercises: Level 2

# The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list and find the min and max age
ages.sort()
print(ages)
print(max(ages))
print(min(ages))

# Add the min age and the max age again to the list
ages.append(min(ages))
ages.append(max(ages))
print(ages)

# Find the median age (one middle item or two middle items divided by two)
ages.sort()
print(len(ages))
median = ages[5:7] 
print(median)
a,b = median
median = (a+b)/2
print(f"median is {median}")

# Find the average age (sum of all items divided by their number )
mean = sum(ages) / len(ages)
print(f"mean of {ages} is {sum(ages)}/{len(ages)} \n mean = {mean}")

# Find the range of the ages (max minus min)
print(f"Range = {max(ages) - min(ages)}")

# Compare the value of (min - average) and (max - average), use abs() method

min_mean = abs(mean - min(ages))
max_mean = abs(mean - max(ages))

print(f"the difference between the min. and the average is {min_mean}")
print(f"the difference between the max. and the average is {max_mean}")

# Find the middle country(ies) in the countries list
country_list = countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]
print(len(country_list))
middle_country = country_list[len(country_list) // 2]
print(middle_country)

# Divide the countries list into two equal lists if it is even if not one more country for the first half.
def divide_lst(lst):
    length = len(lst)
    middle_index = length // 2
    list1 = lst[ : middle_index]
    list2 = lst[middle_index : ]
    print(list1)
    print(list2)

print(divide_lst(country_list))

# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.

min_countries =['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
scandic_countries = min_countries[0:3]
print(scandic_countries)