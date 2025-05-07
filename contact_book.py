# Step 1: Create an empty dictionary to store contacts
contacts = {}

# Step 2: Define functions for different actions

def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    contacts[name] = phone
    print(f"Contact {name} added.")

def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        print("\n--- Contact List ---")
        for name, phone in contacts.items():
            print(f"{name}: {phone}")

def search_contact():
    name = input("Enter name to search: ")
    if name in contacts:
        print(f"{name}'s number is {contacts[name]}")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted.")
    else:
        print("Contact not found.")

# Step 3: Menu loop

while True:
    print("\n--- Contact Book Menu ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")