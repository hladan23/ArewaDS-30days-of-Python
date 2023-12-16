# Exercise: Level 1
import random
import string

def random_user_id():
    characters = string.ascii_lowercase + string.digits
    user_id = ''.join(random.choice(characters) for _ in range(6))
    return user_id
# Example 
print(random_user_id())


def user_id_gen_by_user():

    num_characters = int(input("Enter the number of characters for each ID: "))
    num_ids = int(input("Enter the number of IDs to generate: "))

    print("Error: Please enter valid numeric values.")
    return

    if num_characters <= 0 or num_ids <= 0:
        print("Error: Both values must be greater than zero.")
        return

    user_ids = []
    characters = string.ascii_lowercase + string.digits

    for _ in range(num_ids):
        user_id = ''.join(random.choice(characters) for _ in range(num_characters))
        user_ids.append(user_id)

    return user_ids

# Example 
generated_ids = user_id_gen_by_user()
print(generated_ids)


def rgb_color_gen():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return red, green, blue

# Example
generated_color = rgb_color_gen()
print(f"Generated RGB color: {generated_color}")

# Exercise: Level 2
# Q1

def list_of_hexa_colors(num_colors):
    hexa_colors = []

    for _ in range(num_colors):
        color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        hexa_colors.append(color)

    return hexa_colors
 

def list_of_hexa_colors(num_colors):
    hexa_colors = []

    for _ in range(num_colors):
        color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        hexa_colors.append(color)

    return hexa_colors

# Example 
num_colors_to_generate = 5  
generated_colors = list_of_hexa_colors(num_colors_to_generate)
print(generated_colors)

# Q2
def list_of_rgb_colors(num_colors):
    rgb_colors = []

    for _ in range(num_colors):
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        color = (red, green, blue)
        rgb_colors.append(color)

    return rgb_colors

# Example 
num_colors_to_generate = 5  
generated_colors = list_of_rgb_colors(num_colors_to_generate)
print(generated_colors)

#Q3
def generate_colors(num_colors, color_format='hexa'):
    colors = []

    for _ in range(num_colors):
        if color_format == 'hexa':
            color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        elif color_format == 'rgb':
            red = random.randint(0, 255)
            green = random.randint(0, 255)
            blue = random.randint(0, 255)
            color = (red, green, blue)
        else:
            print("Error: Invalid color format. Please use 'hexa' or 'rgb'.")
            return
               
        
        colors.append(color)

    return colors

# Example
num_colors_to_generate = 5 
generated_hexa_colors = generate_colors(num_colors_to_generate, 'hexa')
print("Generated Hexa Colors:", generated_hexa_colors)

generated_rgb_colors = generate_colors(num_colors_to_generate, 'rgb')
print("Generated RGB Colors:", generated_rgb_colors)


# Exercise: Level 3
# Q1
def shuffle_list(input_list):
    shuffled_list = input_list.copy()  
    random.shuffle(shuffled_list)
    return shuffled_list

# Example
original_list = [1, 2, 3, 4, 5]
shuffled_result = shuffle_list(original_list)
print("Original List:", original_list)
print("Shuffled List:", shuffled_result)
# Q2
def seven_unique_random_numbers():
    unique_numbers = random.sample(range(10), 7)
    return unique_numbers

# Example
result = seven_unique_random_numbers()
print("Seven Unique Random Numbers:", result)

