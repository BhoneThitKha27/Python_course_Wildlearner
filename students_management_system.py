students = []

def add_student():
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    grade = input("Enter student grade: ")
    student = {"name": name, "age": age, "grade": grade}
    students.append(student)
    print(f"{name} added successfully!")

def view_students():
    if not students:
        print("No students in the system.")
    else:
        print("\n--- Student List ---")
        for i, student in enumerate(students, start=1):
            print(f"{i}. Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")

def remove_student():
    if not students:
        print("No students to remove.")
    else:
        view_students()
        try:
            index = int(input("Enter the number of the student to remove: "))
            if 1 <= index <= len(students):
                removed = students.pop(index - 1)
                print(f"{removed['name']} removed successfully.")
            else:
                print("Invalid number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Remove Student")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            remove_student()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()