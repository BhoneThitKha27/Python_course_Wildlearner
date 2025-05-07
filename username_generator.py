# Step 1: Get user input
first_name = input("Enter your first name: ").lower()
last_name = input("Enter your last name: ").lower()

# Step 2: Validate birth year
while True:
    birth_year = input("Enter your birth year (e.g. 2001): ")
    if birth_year.isdigit() and len(birth_year) == 4:
        break
    else:
        print("Invalid year. Please enter a 4-digit number like 2001.")

# Step 3: Generate username options
username1 = first_name + last_name
username2 = first_name[0] + last_name + birth_year[-2:]
username3 = last_name + "_" + first_name
username4 = first_name + str(len(last_name)) + birth_year[:2]

# Step 4: Display options
print("\nHere are some username suggestions for you:")
print("1.", username1)
print("2.", username2)
print("3.", username3)
print("4.", username4)