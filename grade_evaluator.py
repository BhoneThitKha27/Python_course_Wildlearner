# Step 1: Get user input for marks
try:
    marks = float(input("Enter your score (0 - 100): "))

    # Step 2: Check for valid input range
    if marks < 0 or marks > 100:
        print("Invalid score! Please enter a value between 0 and 100.")
    else:
        # Step 3: Evaluate the grade based on score
        if marks >= 90:
            grade = "A"
        elif marks >= 80:
            grade = "B"
        elif marks >= 70:
            grade = "C"
        elif marks >= 60:
            grade = "D"
        else:
            grade = "F"

        # Step 4: Print the result
        print(f"Your grade is: {grade}")

except ValueError:
    print("Error: Please enter a valid number!")