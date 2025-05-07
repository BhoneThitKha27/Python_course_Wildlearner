# Step 1: Get user input for the year
try:
    year = int(input("Enter a year to check if it's a leap year: "))

    # Step 2: Apply leap year logic
    if (year % 4 == 0):
        if (year % 100 == 0):
            if (year % 400 == 0):
                print(f"{year} is a leap year.")
            else:
                print(f"{year} is not a leap year.")
        else:
            print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")

except ValueError:
    print("Error: Please enter a valid year (integer).")