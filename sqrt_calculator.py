import math as sq

num = float(input("Enter a Number: "))
try:
    ans = sq.sqrt(num)
    print(f"The squartroot of {num} is {ans} ")
except:
    print("Error, Please enter a valid no.")