# Ethan Lawrence
# Nov 13 2024
# Practice: Positional & Keyword Arguments in Python


# POSITIONAL ARGUMENTS
# Start by writing the code to create the three functions outlined below
# You'll use only positional arguments in the first three functions
# Test your code and correct any errors

# Greet The User
# Write a function that takes two parameters -- first name and age
# Use an f-string to welcome the user by first name and to display his/her age
def greet(fname, age):
    print(f'Hello {fname}, you are {age} years old.')
greet('John', '26')

# Area of a Rectangle
# Write a function to calculate the area (in square feet) of a rectangle
# Your two parameters will be length and width
# The print statement in the function should display the length, width and area (in square feet) of your rectangle
def calc_area(length, width):
    print(f'{length * width}ft^2')
calc_area(10, 20)

# Sum of Numbers
# Write a function that finds the sum of three numbers
# Your three parameters will be num1, num2, and num3
# The print statement in the function should display the sum of the three numbers

def sum_of_3(num1, num2, num3):
    print(num1 + num2 + num3)
sum_of_3(18, 28, 38)

# KEYWORD ARGUMENTS
# Create the three functions outlined below
# In these last three functions, you'll use only keyword arguments 
# Test your code and correct any errors

# Greet By Title
# Write a function that greets the user by title, first name and last name
# Examples of titles include: Mr., Ms., Mrs. and Dr.
# When calling your function, change the order of your keyword arguments so that they don't match the order of your function parameters
def greet_by_title(title, first_name, last_name):
    print(f'Hello {title}. {first_name} {last_name}')
greet_by_title(title = 'Mr', last_name = 'Doe', first_name = 'John')

# Describe Your Pet
# Write a function that says what type of pet you have and what your pet's name is
# Your function parameters will be pet_type and pet_name
def pet(pet_type, pet_name):
    print(f'I have a {pet_type} their name is {pet_name}.')
pet(pet_name = 'Jack', pet_type = 'Dog')
# Updated Function
# Choose any ONE of the first three functions from this project and rewrite it below using keyword arguments
def greet(fname, age):
    print(f'Hello {fname}, you are {age} years old.')
greet(age = '26', fname = 'John')