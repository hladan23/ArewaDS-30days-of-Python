# Exercise: Level 1
for i in range(11):
    print(i)
i = 0

while i <= 10:
    print(i)
    i += 1
for i in range(10, -1, -1):
    print(i)
    
i = 10
while i >= 0:
    print(i)
    i -= 1
    
for i in range(1, 8):
    print('*' * i)
for i in range(8):
    for j in range(8):
        print("#", end=" ")
    print()  # Move to the next line after each row
    
for i in range(11):
    result = i * i
    print(f"{i} x {i} = {result}")
    
my_list = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for item in my_list:
    print(item)
    
for number in range(0, 101, 2):
    print(number)

for number in range(1, 101, 2):
     print(number)
     
# Exercise:Level 2
sum_of_numbers = 0

for number in range(101):
    sum_of_numbers += number
print(f"The sum of all numbers is {sum_of_numbers}.")

sum_of_evens = 0
sum_of_odds = 0

for number in range(101):
    if number % 2 == 0:
        sum_of_evens += number
    else:
        sum_of_odds += number

print(f"The sum of all evens is {sum_of_evens}.")
print(f"The sum of all odds is {sum_of_odds}.")

# Exercise: Level 3
from data.countries import countries

    
   
    

   
