# Q1
numbers = [1, -2, 0, 3, -4, 5, 0, -6, 7]

filtered_numbers = [num for num in numbers if num <= 0]

print("Filtered Numbers (Negative and Zero):", filtered_numbers)

# Q2
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

flattened_list = [num for sublist in list_of_lists for inner_list in sublist for num in inner_list]

print("Flattened List:", flattened_list)

# Q3
result_list = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]

print(result_list)

# Q4
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

output = [[country.upper(), country[:3].upper(), capital.upper()] for sublist in countries for (country, capital) in sublist]

print(output)

# Q5
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

output = [{'country': country.upper(), 'city': city.upper()} for sublist in countries for (country, city) in sublist]

print(output)

# Q6
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

output = [' '.join(name) for sublist in names for name in sublist]

print(output)

# Q7
# Lambda function to calculate the slope of a linear function (m)
slope_function = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)

# Lambda function to calculate the y-intercept of a linear function (b)
y_intercept_function = lambda x, y, m: y - m * x

# Example
# For the points (x1, y1) = (1, 2) and (x2, y2) = (3, 4)
slope_result = slope_function(1, 2, 3, 4)
y_intercept_result = y_intercept_function(1, 2, slope_result)

print("Slope:", slope_result)
print("Y-Intercept:", y_intercept_result)





