"""
LESSON 02: USER INPUT AND TYPE CONVERSION

The input() function allows a Python program to receive information
from the user.

By default, input() returns the entered value as a string (str).

In this lesson, we will learn:

1. Using input()
2. Checking input data types
3. Converting strings to integers using int()
4. Converting strings to floats using float()
5. Converting values using str()
6. Performing calculations with converted input
7. Practical example
"""

# -----------------------------------
# 1. Basic User Input
# -----------------------------------

name = input("Enter your name: ")

print(f"Hello, {name}!")
print(f"Data type: {type(name)}")

# -----------------------------------
# 2. Input Data Type
# -----------------------------------

age = input("Enter your age:") 

print(f"Age: {age}")
print(f"Data type: {type(age)}")

# -----------------------------------
# 3. Converting String to Integer
# -----------------------------------

age = int(age) # Convert the string input to an integer

print(f"Age after conversion: {age}")
print(f"Data type: {type(age)}")

# -----------------------------------
# 4. Calculations with Converted Input
# -----------------------------------

age_next_year = age + 1

print(f"Next year you will be {age_next_year} years old.")

age_in_5_years = age + 5 

print(f"In 5 years you will be {age_in_5_years} years old.")

# -----------------------------------
# 5. Converting String to Float
# -----------------------------------

height_text = input("Enter your height in feet: ")

print(f"Height before conversion: {height_text}")
print(f"Data type before conversion: {type(height_text)}")

height = float(height_text)

print(f"Height after conversion: {height}")
print(f"Data type after conversion: {type(height)}")

height_in_centimeters = height * 30.48 # Convert height from feet to centimeters

print(f"Height in centimeters: {height_in_centimeters:.2f} cm")

# -----------------------------------
# 6. Converting Values to String
# -----------------------------------

score = 95

print(f"Score: {score}")
print(f"Data type before conversion: {type(score)}")

score_text = str(score) #Convert the integer score to a string 
print(f"Score after conversion: {score_text}")
print(f"Data type after conversion: {type(score_text)}")

# -----------------------------------
# 7. Practical Example
# -----------------------------------

print("-----------Personal Information--------------")
name = input("Enter your name: ")
age = int(input("Enter your age: ")) # Convert the string input to an integer
height = float(input("Enter your height in feet: ")) # Convert the string input to a float

print(f"name: {name}")
print(f"age: {age}")
print(f"height: {height:.2f} feet")

age_in_5_years = age + 5 
height_in_centimeters = height * 30.48 

print("-----------Calculations--------------")
print(f"In 5 years you will be {age_in_5_years} years old")
print(f"Your height is {height_in_centimeters:.2f} cm")
