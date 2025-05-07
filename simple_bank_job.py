# Bank system using only basic Python functions

accounts = {}

def create_account():
    name = input("Enter your name: ")
    if name in accounts:
        print("Account already exists.")
    else:
        accounts[name] = 0.0
        print(f"Account created for {name}.")

def deposit():
    name = input("Enter your name: ")
    if name in accounts:
        try:
            amount = float(input("Enter amount to deposit: "))
            if amount > 0:
                accounts[name] += amount
                print(f"${amount} deposited. New balance: ${accounts[name]}")
            else:
                print("Amount must be positive.")
        except ValueError:
            print("Invalid amount.")
    else:
        print("Account not found.")

def withdraw():
    name = input("Enter your name: ")
    if name in accounts:
        try:
            amount = float(input("Enter amount to withdraw: "))
            if 0 < amount <= accounts[name]:
                accounts[name] -= amount
                print(f"${amount} withdrawn. New balance: ${accounts[name]}")
            else:
                print("Invalid amount or insufficient funds.")
        except ValueError:
            print("Invalid amount.")
    else:
        print("Account not found.")

def check_balance():
    name = input("Enter your name: ")
    if name in accounts:
        print(f"Current balance: ${accounts[name]}")
    else:
        print("Account not found.")

# Main program loop
while True:
    print("\n=== Simple Bank Menu ===")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        create_account()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        check_balance()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")