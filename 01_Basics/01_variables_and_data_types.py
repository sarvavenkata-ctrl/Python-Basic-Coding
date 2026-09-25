"""
LESSON 01: VARIABLES AND DATA TYPES

A variable is a name used to store data in a Python program.

Python has several built-in data types. In this lesson, we will learn:

1. String (str)   - Text
2. Integer (int)  - Whole numbers
3. Float (float)  - Decimal numbers
4. Boolean (bool) - True or False

We will also use type() to check the data type of a variable.
"""
# -----------------------------------
# 1. String
# -----------------------------------

name = "Sarva"

print(f"Name: {name}")
print(f"Data type: {type(name)}")

# -----------------------------------
# 2. Integer
# -----------------------------------

age = 25

print(f"Age: {age}")
print(f"Data type: {type(age)}")

# -----------------------------------
# 3. Float
# -----------------------------------

height = 5.9

print(f"Height: {height}")
print(f"Data type: {type(height)}")

# -----------------------------------
# 4. Boolean
# -----------------------------------

is_student = True

print(f"Is Student: {is_student}")
print(f"Data type: {type(is_student)}")

# -----------------------------------
# 5. Variable Naming Rules
# -----------------------------------

# Variable names should be descriptive.
# They can contain letters, numbers, and underscores.
# They cannot start with a number.
# Python variable names are case-sensitive.
# snake_case is commonly used for variable names.

first_name = "Sarva"
student_age = 25
course_name = "Python"
course_duration = 2
is_online = True 

print(f"First name: {first_name}")
print(f"Student age: {student_age}")
print(f"Course: {course_name}")
print(f"Duration: {course_duration} months")
print(f"Is online: {is_online}")

#-----------------------------------
#6. Pratical Example 
#-----------------------------------
student_name = "Srava"
student_age = 25
python_level = "Beginner"
python_level = "Intermediate"
is_learning = True

print("---------- Student Information ----------")
print(f"Student name: {student_name}")
print(f"Student age: {student_age}")
print(f"Python level: {python_level}")

print("---------- Updated Learning Status ----------")
python_level = "Intermediate"

print(f"Updated Python level: {python_level}")
print(f"Currently learning: {is_learning}") 