# ============================================================
# LESSON 06: LISTS
# ============================================================

# Definition:
# A list is a Python data structure used to store multiple
# values in a single variable.

# Why do we use lists?
# Lists help us organize and manage multiple related values
# instead of creating a separate variable for every value.

# Where are lists used?
# - Storing names of students or employees
# - Storing product names or prices
# - Creating shopping lists
# - Storing marks or scores
# - Working with datasets
# - Processing multiple values using loops
# - Data analysis and machine learning

# Important features of lists:
# - Lists are ordered.
# - Lists can contain multiple values.
# - List items can be changed.
# - Lists allow duplicate values.
# - Items are accessed using indexes.
# - Python list indexing starts at 0.
# ============================================================
# LESSON 06: LISTS
# ============================================================

# Definition:
# A list is a Python data structure used to store multiple
# values in a single variable.

# Why do we use lists?
# Lists help us organize and manage multiple related values
# instead of creating a separate variable for every value.

# Where are lists used?
# - Storing names of students or employees
# - Storing product names or prices
# - Creating shopping lists
# - Storing marks or scores
# - Working with datasets
# - Processing multiple values using loops
# - Data analysis and machine learning

# Important features of lists:
# - Lists are ordered.
# - Lists can contain multiple values.
# - List items can be changed.
# - Lists allow duplicate values.
# - Items are accessed using indexes.
# - Python list indexing starts at 0.

# -----------------------------------
# 1. Creating and Accessing a List
# -----------------------------------

students = ["Sarva", "John", "Alex"]

print(students)
print(students[0])
print(students[1])
print(students[2])

# -----------------------------------
# 2. Changing an Item in a List
# -----------------------------------

print("Before changing:", students)
students[1] = "David"
print("After changing:", students)

# -----------------------------------
# 3. Adding Items to a List
# -----------------------------------

students = ["Sarva", "John", "Alex"]
print("Before append:", students)
students.append("David")
print("After append:", students)

print("-------------using insert()--------------")

students = ["Sarva", "John", "Alex"]

print("Before insert:", students)
students.insert(2, "David")
print("After insert:", students)

# -----------------------------------
# 4. Removing Items from a List
# -----------------------------------

# Definition:
# remove() deletes the first occurrence of a specified value.

# Where is it used?
# - Removing students from a class list
# - Removing unavailable products
# - Updating shopping lists

print("-------------------using remove-----------------")

students = ["Sarva", "John", "Alex", "David", "wait"]
print("Before remove:", students)
students.remove("wait")
print("After remove:" , students)

# -----------------------------------
# 4.2 Removing Items Using pop()
# -----------------------------------

# Definition:
# pop() removes an item at a specified index.
# It also returns the removed item.

# Where is it used?
# - Removing an item by its position
# - Processing the last item in a list
# - Managing a stack of tasks

print("-------------using pop----------")

students = ["Sarva", "Alex", "David", "John", "Wait"]
print("Before pop:", students)
removed_students  = students.pop(4)
print("Removed studet:", removed_students)
print("After pop:", students)

# -----------------------------------
# 5. Counting Items Using len()
# -----------------------------------

# Definition:
# len() returns the number of items in a list.

# Where is it used?
# - Counting students
# - Counting products
# - Checking the size of a dataset

print("------------using lens()--------------")

languages = ["Python", "C++", "JavaScript", "SQL", "Java"]

print ("Programming languages:", languages)

Total_languages = len(languages)

print("Number of programming languages:", Total_languages)

# -----------------------------------
# 6. Looping Through a List
# -----------------------------------

# Definition:
# A for loop processes each item in a list one at a time.

# Why do we use it?
# To process multiple values without repeating code.

# Where is it used?
# - Processing student marks
# - Displaying products
# - Analysing datasets
# - Preparing data for machine learning

print("-------------Looping through a List------------")

languages = ["Python", "Java", "C++", "Java Script", "SQL"]

for language in languages :
    print(language)
 
#Multiplying numbers using Loops 

print("---------------Multipying List Items-----------------")

numbers = [2, 4, 6]

for number in numbers:
    result = number * 2
    print(f"{number} x 2 = {result}")        

# -----------------------------------
# 7. Practical Example: Student Marks Analysis
# -----------------------------------

# Definition:
# This program stores student marks in a list
# and helps us analyse student performance.

# Where is it used?
# - Student performance analysis
# - Calculating average scores
# - Data analysis and machine learning

print("-------------Student marks Analysis----------")

marks = [75, 80, 90, 85, 70]

print("Student marks:", marks)
total_students = len(marks)
print("Total students:", total_students)

# -----------------------------------
# 7.2 Calculating Total Marks
# -----------------------------------

# Definition:
# A running total adds each value from a list
# to a variable that stores the accumulated result.

print("-------------Calculting Total Marks-------------")

total_marks = 0

for mark in marks:
    total_marks += mark

print("Total marks:", total_marks)


# -----------------------------------
# 7.3 Calculating Average Marks
# -----------------------------------

# Definition:
# Average is the sum of all marks divided
# by the total number of students.

# Where is it used?
# - Student performance analysis
# - Data analysis
# - Machine learning preprocessing

print("---------------Calculating Average-------------")

average_marks = total_marks/total_students

print(f"Average marks:{average_marks:.2f}")
