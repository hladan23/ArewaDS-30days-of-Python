age = 35
height = 21.5
complex = 5+5j

base = float(input("Enter Base: "))
height = float(input("Enter height: "))
area = 0.5 * base * height
print(f"The area of the triangle is {area}")

a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
perimeter = a + b + c
print(f"The perimeter of the triangle is {perimeter}")

length = float(input("Enter Length: "))
width = float(input("Enter Width: "))
area = length * width
perimeter = 2 * (length + width)
print(f"the area of the rectangle is {area}, and the perimeter is {perimeter} ")

radius = float(input("Enter Radius: "))
pi = 3.14
area = pi * radius**2
circumference = 2 *pi * radius
print(f"the area of the circle is {area} a3nd the circumference is {circumference}")


y = lambda x: 2 * x - 2
sl1 = (y(1) - y(0)) / (1 - 0)
print(f"The slope is{sl1}")

import math
x1 = 2
y1 = 2
x2 = 6
y2 = 10
sl2 = (y2-y1)/(x2-x1)
print(f"the slope is {sl2}")
pnt = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f"The Euclidian distance between (2, 2) and (6, 10) is {pnt}")

print(sl1 == sl2)

def y(x):
    return x**2 + 6*x + 9
print("y(0) =", y(0))
print("y(-1) =", y(-1))
print("y(-2) =", y(-2))
print("y(-3) =", y(-3))
print("y(-4) =", y(-4))
print("y(-5) =", y(-5))

print("You can see that y is 0 when x is -3. This means that -3 is the root of the equation y = x^2 + 6x + 9")

xt,xy = len("python"), len("dragon")
print(xt != xy )

print("on" in "python" and "dragon")

print("jargon" in "I hope this course is not full of jargon")

print("on" not in "python" and "dragon")

ln = len("python")
ln = float(n)
ln = str(n)
print(f"{ln} and {type(ln)}")

ev = float(input("Enter no:"))
if ev % 2 == 0:
    print("this is an even number")
else:
    print("this is an odd number")

print(7 // 3 == int(2.7))

print(type('10') == type(10))

print(int(9.8) == 10)

hours = float(input("Enter hours: "))
rt = float(input("Enter rate per hour: "))
weekly = hrs * rt
print(f"Your weekly earning is {weekly}")

years = float(input("Enter number of years you have lived: "))
secs = years * 365 * 24 * 60 * 60
print(f"You have lived for {secs}seconds.")

print('''
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125'''  
)