# Student Attendance Management System (Console-Based)
# Author: Rehan Ali Sayyed
# Description: A complete Python project for managing students and their attendance

import datetime

students = {}
attendance_records = {}

# ------------------ Utility Functions ------------------

def generate_student_id():
    return f"STU{len(students)+1:03d}"

# ------------------ Core Functions ------------------

def add_student():
    name = input("Enter student name: ").strip()
    course = input("Enter course/class: ").strip()
    sid = generate_student_id()
    students[sid] = {"name": name, "course": course}
    print(f"\nStudent added successfully! ID: {sid}\n")


def view_students():
    if not students:
        print("\nNo students found.\n")
        return
    print("\n--- Student List ---")
    for sid, info in students.items():
        print(f"ID: {sid} | Name: {info['name']} | Course: {info['course']}")
    print()


def mark_attendance():
    if not students:
        print("\nNo students available. Please add students first.\n")
        return

    date = datetime.date.today().isoformat()
    if date not in attendance_records:
        attendance_records[date] = {}

    for sid in students:
        status = input(f"Is {students[sid]['name']} present? (P/A): ").upper()
        if status not in ('P', 'A'):
            print("Invalid input, marked Absent by default.")
            status = 'A'
        attendance_records[date][sid] = "Present" if status == 'P' else "Absent"

    print("\nAttendance marked successfully!\n")


def view_attendance():
    if not attendance_records:
        print("\nNo attendance records available.\n")
        return

    for date, records in attendance_records.items():
        print(f"\nDate: {date}")
        for sid, status in records.items():
            name = students[sid]['name'] if sid in students else "Unknown Student"
            print(f"  {name} ({sid}) : {status}")
    print()


def student_report():
    sid = input("Enter Student ID: ").strip()
    if sid not in students:
        print("\nInvalid Student ID.\n")
        return

    present = 0
    total = 0
    for records in attendance_records.values():
        if sid in records:
            total += 1
            if records[sid] == "Present":
                present += 1

    if total == 0:
        print("\nNo attendance data for this student.\n")
    else:
        percentage = (present / total) * 100
        print(f"\nAttendance Report for {students[sid]['name']}")
        print(f"Present: {present}/{total}")
        print(f"Attendance Percentage: {percentage:.2f}%\n")

# ------------------ Main Menu ------------------

def main_menu():
    while True:
        print("===== Student Attendance Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Mark Attendance")
        print("4. View Attendance")
        print("5. Student Attendance Report")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            mark_attendance()
        elif choice == '4':
            view_attendance()
        elif choice == '5':
            student_report()
        elif choice == '6':
            print("\nThank you for using the system. Goodbye!\n")
            break
        else:
            print("\nInvalid choice. Try again.\n")


if __name__ == "__main__":
    main_menu()
