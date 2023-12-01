
print( 'Thirty '+ 'Days ' + 'Of ' + 'Python' )

print( 'Coding'+ 'For' + 'All')

company =  "Coding For All"

print(company)

print(len(company))

print(company.upper())

print(company.lower())

text = "Coding For All"
print(text.capitalize())
print(text.title())
print(text.swapcase())

print(text[0:6])

print(text.find("Coding"))

print(text.replace("Coding", "Python"))

s = "Python for Everyone"
print(s.replace("Everyone", "All"))

co = 'Coding For All'
print(ch.split()) 

co = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(ch.split(','))

gg = "Coding For All" 
print(gg[0]) #C

print(gg[-1]) #l

print(gg[10]) #" "

acc = 'Python For Everyone'
print(".".join(word[0] for word in acc.split()))

acc = 'Coding For All'
print(".".join(word[0] for word in acc.split()))

text = "Coding For All"
print(text.index("C"))

text = "Coding For All"
print(text.index("F"))

text = "Coding For All People"
position = text.rfind("l")
print(position)

text = "You cannot end a sentence with because because because is a conjunction"
position = text.index("because")
print(position)

position = text.rindex("because")
print(position)

phrase = text[31:54]
print(phrase)

text = "You cannot end a sentence with because because because is a conjunction"
position = text.index("because")
print(position)

phrase = text[31:54]
print(phrase)

text = 'Coding For All' 
print(text.startswith('Coding')) #true

text = 'Coding For All' 
print(text.startswith('coding')) #False

challenge = '   Coding For All      '
print(challenge.strip(' '))

chn = '30DaysOfPython'
print(chn.isidentifier()) # False, because it starts with a number
chn = 'thirty_days_of_python'
print(chn.isidentifier()) # True

python_libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
result = '# '.join(python_libraries)
print(result)

print("I am enjoying this challenge.\nI just wonder what is next.")

print("Name\t        Age  \tCountry \tCity")
print("Asabeneh\t250\tFinland \tHelsinki")

print('{} = {}'.format('radius', 10))
radius = 10
print('{} = {} * {} ** {}'.format('area', 3.14,  'radius', 2))
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {area} meters square.")

a=8
b=6
print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b))
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))