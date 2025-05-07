# Step 1: Get user input
try:
    number = int(input("Enter a number to generate its multiplication table: "))
    limit = int(input("Enter how far the table should go (e.g., 10): "))

    # Step 2: Use a loop to generate and print the table
    print(f"\nMultiplication table for {number}:\n")
    for i in range(1, limit + 1):
        result = number * i
        print(f"{number} x {i} = {result}")

except ValueError:
    print("Error: Please enter valid integers only.")