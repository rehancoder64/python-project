import csv

FILENAME = "students.csv"

def add_student():
    name = input("Enter student name: ")
    subject = input("Enter subject: ")
    marks = int(input("Enter marks (0-100): "))

    with open(FILENAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, subject, marks])

    print("Student added successfully!\n")

def view_students():
    try:
        with open(FILENAME, "r") as file:
            reader = csv.reader(file)
            print("\nStudent Records:")
            print("Name | Subject | Marks")
            print("----------------------")
            for row in reader:
                print(f"{row[0]} | {row[1]} | {row[2]}")
            print()
    except FileNotFoundError:
        print("No records found.\n")

def calculate_average():
    total = 0
    count = 0

    try:
        with open(FILENAME, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                total += int(row[2])
                count += 1

        if count == 0:
            print("No students available.\n")
        else:
            average = total / count
            print(f"Average Marks: {average:.2f}\n")

    except FileNotFoundError:
        print("No data file found.\n")

def menu():
    while True:
        print("STUDENT MANAGEMENT SYSTEM")
        print("1. Add Student")
        print("2. View Students")
        print("3. Calculate Average Marks")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            calculate_average()
        elif choice == "4":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

menu()
