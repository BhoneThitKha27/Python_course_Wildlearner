# Unit Converter

# Step 1: Define conversion factors relative to meters
conversion_factors = {
    'meter': 1.0,
    'kilometer': 1000.0,
    'centimeter': 0.01,
    'millimeter': 0.001,
    'mile': 1609.34,
    'yard': 0.9144,
    'foot': 0.3048,
    'inch': 0.0254
}

try:
    # Step 2: Get user input for the value and convert it to float
    value = float(input("Enter the value to convert: "))

    # Normalize unit inputs by converting to lowercase
    from_unit = input("Enter the unit to convert from: ").lower()
    to_unit = input("Enter the unit to convert to: ").lower()

    # Step 3: Check if both units are valid
    if from_unit in conversion_factors and to_unit in conversion_factors:
        # Convert from source unit to meters
        value_in_meters = value * conversion_factors[from_unit]

        # Convert from meters to target unit
        converted_value = value_in_meters / conversion_factors[to_unit]

        # Output the result using f-string formatting
        print(f"{value} {from_unit} is equal to {converted_value} {to_unit}")
    else:
        # Handle invalid unit names
        print("Error: One or both units are not recognized. Please check spelling.")

except ValueError:
    # Handle case where input for value is not a number
    print("Error: Please enter a valid number for the value to convert.")