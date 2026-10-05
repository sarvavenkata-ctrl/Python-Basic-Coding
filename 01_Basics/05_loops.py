# -----------------------------------
# 1. for Loop
# -----------------------------------

for number in range(5):
    print(number)

print("-------------counting from 1 to 5------------")
for number in range(1, 6):
    print(number)

print("---------------Learning python loop-----------------")
for day in range(1, 6):
    print(f"Day {day} : Learning Python")

#----------------------------------
# 2. Calculations inside a loop
#---------------------------------
print("---------------Calculating Square of a number-----------------")
for number in range(1, 6):
    square = number ** 2
    print(f"{number} square = {square}")

# -----------------------------------
# 3. Looping Through a List
# -----------------------------------
print("--------------Looping through a list of programming languages-----------------")
languages = ["Python", "JavaScript", "Java", "C++"]

for language in languages:
    print(language)

# -----------------------------------
# 4. Loop with a Conditional Statement
# -----------------------------------

print(f"-----------------looping through a list of numbers by using conditions----------------")
numbers = [1, 2, 3, 4, 5]

for number in numbers:
    if number >= 3:
        
        print(number)

# -----------------------------------
# 5. while Loop
# -----------------------------------

print ("--------------while loop ----------------")
count = 1
while count <= 5:
    print(count)
    count += 1 

# -----------------------------------
# 6. Practical Example - Multiplication Table
# -----------------------------------
print("-------------Multiplication Table----------------")

number = 5
for multiplier in range(1, 6):
    result = number * multiplier
    print(f"{number} * {multiplier} = {result}")






    
