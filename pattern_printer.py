# Step 1: Get number of rows from user
rows = int(input("Enter number of rows: "))

# Step 2: Loop to print the pattern

for i in range(1, rows + 1):
    print("*" * i)

for i in range(rows, 0, -1):
    print("*" * i)
    
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * i)