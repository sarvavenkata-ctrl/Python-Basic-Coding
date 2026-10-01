"""
LESSON 03: OPERATORS

Operators are symbols or keywords used to perform operations
on values and variables.

In this lesson, we will learn:

1. Arithmetic operators
2. Assignment operators
3. Comparison operators
4. Logical operators
5. Practical example
"""
# -----------------------------------
# 1. Arithmetic Operators
# -----------------------------------

number_1 = 10
number_2 = 3

addition = number_1 + number_2 
subtraction = number_1 - number_2
multiplication = number_1 * number_2
division = number_1 / number_2
floor_division = number_1 // number_2
remainder = number_1 % number_2
power = number_1 ** number_2


print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")
print(f"Floor Division: {floor_division}")
print(f"Remainder: {remainder}")
print(f"Power: {power}")

# -----------------------------------
# 2. Assignment Operators
# -----------------------------------

score = 10 

score += 5 # score = score + 5 
print(f"after += 5: {score}")
score -= 3 # score = score - 3
print(f"after -= 3: {score}")
score *= 2# score = score * 2
print(f"after *= 2: {score}")
score /= 4 # score = score / 4
print(f"after /= 4: {score}")

# -----------------------------------
# 3. Comparison Operators
# -----------------------------------

number_1 = 10 
number_2 = 5

print(f"Equal: {number_1 == number_2}")
print(f"Not equal: {number_1 != number_2}")
print(f"Greater than: {number_1 > number_2}")
print(f"Less than: {number_1 < number_2}")
print(f"Greater than or equal to: {number_1 >= number_2}")
print(f"Less than or equal to: {number_1 <= number_2}")

# ----------------------------------- 
# 4. Logical Operators
# -----------------------------------

age = 25
has_id = True

print(f"AND: {age >= 18 and has_id}")

is_student = False
has_discount_code = True

print(f"OR: {is_student or has_discount_code}")

is_logged_in = True

print(f"NOT: {not is_logged_in}")

# -----------------------------------
# 5. Practical Example
# -----------------------------------

purchase_amount = 75
is_member = True 
discount_eligible = purchase_amount >= 50 and is_member

print(f"Discount eligible: {discount_eligible}")

discount_amount = purchase_amount * 10 / 100
final_amount = purchase_amount - discount_amount 

print(f"Discount: £{discount_amount:.2f}")
print(f"Final amount: £{final_amount:.2f}")