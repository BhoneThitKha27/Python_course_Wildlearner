# Function to check password strength
def check_password_strength(password):
    strength = 0
    remarks = []

    # Length check
    if len(password) >= 8:
        strength += 1
    else:
        remarks.append("Password is too short (minimum 8 characters)")

    # Check for uppercase letters
    has_upper = False
    for char in password:
        if char.isupper():
            has_upper = True
            break
    if has_upper:
        strength += 1
    else:
        remarks.append("Add at least one uppercase letter")

    # Check for lowercase letters
    has_lower = False
    for char in password:
        if char.islower():
            has_lower = True
            break
    if has_lower:
        strength += 1
    else:
        remarks.append("Add at least one lowercase letter")

    # Check for numbers
    has_digit = False
    for char in password:
        if char.isdigit():
            has_digit = True
            break
    if has_digit:
        strength += 1
    else:
        remarks.append("Add at least one number")

    # Check for special characters (manual way)
    special_characters = "!@#$%^&*()-_=+[]{}|;:',.<>/?"
    has_special = False
    for char in password:
        if char in special_characters:
            has_special = True
            break
    if has_special:
        strength += 1
    else:
        remarks.append("Add at least one special character")

    # Strength report
    if strength == 5:
        return "Strong password!"
    elif strength >= 3:
        return "Moderate password. Tips:\n- " + "\n- ".join(remarks)
    else:
        return "Weak password. Tips:\n- " + "\n- ".join(remarks)

# Ask user for password
user_password = input("Enter your password to check strength: ")
result = check_password_strength(user_password)
print("\n" + result)