# Step 1: Set correct username and password
correct_username = "felix"
correct_password = "katana123"

# Step 2: Set attempt counter
attempts = 0
max_attempts = 3

# Step 3: Login attempt loop
while attempts < max_attempts:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_username and password == correct_password:
        print("Login successful! Welcome!")
        break  # exit the loop if login is successful
    else:
        attempts += 1
        print("Incorrect username or password.")
        print(f"Attempts left: {max_attempts - attempts}")

# Step 4: Lock out if too many failed attempts
if attempts == max_attempts:
    print("Too many failed attempts. Access denied.")