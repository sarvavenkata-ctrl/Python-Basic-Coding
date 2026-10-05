# -----------------------------------
# 1. if-else Statement
# -----------------------------------

age = 25

if age >= 18:
    print("You are an adult.")
else:
    print("You are not an adult.")

age = 25

if age >= 18:
    print("You are an adult.")
else:
    print("You are not an adult.")

# -----------------------------------
# 2. if-elif-else Statement
# -----------------------------------

temperature = 35

if temperature >= 30:
    print("It's a hot day.")
elif temperature >= 20:
    print("It's a warm day.")
else:
    print("It's a cold day.")

# -----------------------------------
# 3. Multiple Conditions
# -----------------------------------

is_student = False
has_discount_code = True

if is_student or has_discount_code:
    print("Discount available.")
else:
    print("No discount available.")

is_blocked = False

if not is_blocked:
    print("Access granted.")
else:
    print("Access denied.")

# -----------------------------------
# 4. Practical Example
# -----------------------------------

purchase_amount = 80
is_member = False

if purchase_amount >= 50 and is_member:
    print("You are eligible for 10% discount.")
    discount_amount = purchase_amount * 10 / 100
    final_amount = purchase_amount - discount_amount
    print(f"Discount amount: £{discount_amount:.2f}")
    print(f"Final amount after discount: £{final_amount:.2f}")
else:
    print("You are not eligible for discount.")
    print(f"Final amount to pay:£{purchase_amount:.2f}")





