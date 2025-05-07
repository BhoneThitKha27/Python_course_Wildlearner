# Step 1: Get input from the user
num = int(input("Enter a number to check if it's prime: "))

# Step 2: Handle edge cases
if num <= 1:
    print(f"{num} is not a prime number.")
else:
    is_prime = True  # Assume it is prime

    # Step 3: Check divisibility
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break  # No need to check further

    # Step 4: Output result
    if is_prime:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")