# Tip Calculator

# Step 1: Get user input
bill_amount = float(input("Enter the total bill amount: $"))
tip_percentage = float(input("Enter the tip percentage (e.g., 15 for 15%): "))
num_people = int(input("Enter the number of people splitting the bill: "))

# Step 2: Calculate tip and totals
tip_amount = bill_amount * (tip_percentage / 100)
total_bill = bill_amount + tip_amount
per_person = total_bill / num_people

# Step 3: Display results
print(f"\nTip Amount: ${tip_amount:.2f}")
print(f"Total Bill (with tip): ${total_bill:.2f}")
print(f"Each person should pay: ${per_person:.2f}")