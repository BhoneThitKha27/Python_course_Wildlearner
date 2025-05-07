# Diary App

def show_menu():
    print("\n--- Diary App ---")
    print("1. Write a new entry")
    print("2. View diary entries")
    print("3. Exit")

def write_entry():
    entry = input("Write your diary entry:\n")
    with open("diary.txt", "a") as file:  # Append mode so entries stack up
        file.write(entry + "\n---\n")  # Separate entries by ---
    print("Entry saved!")

def read_entries():
    try:
        with open("diary.txt", "r") as file:
            content = file.read()
            if content:
                print("\nYour Diary Entries:\n")
                print(content)
            else:
                print("No entries yet.")
    except FileNotFoundError:
        print("No diary file found. Start by writing your first entry!")

# Main loop
while True:
    show_menu()
    choice = input("Choose an option (1-3): ")

    if choice == "1":
        write_entry()
    elif choice == "2":
        read_entries()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")