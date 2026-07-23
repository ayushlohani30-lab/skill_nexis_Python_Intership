# Student Management System (CSV File Based)

import csv
import os

FILENAME = "students.csv"
FIELDNAMES = ["Roll Number", "Name", "Marks"]

def initialize_csv():
    """Creates the CSV file with headers if it doesn't already exist."""
    if not os.path.exists(FILENAME):
        with open(FILENAME, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
            writer.writeheader()

def load_students():
    students = []
    if os.path.exists(FILENAME):
        with open(FILENAME, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                students.append(row)
    return students

def save_students(students):
    with open(FILENAME, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(students)

def add_student():
    students = load_students()
    roll = input("Enter Roll Number: ").strip()
    
    # Check for duplicate roll numbers
    for student in students:
        if student["Roll Number"] == roll:
            print(f"Error: Student with Roll Number {roll} already exists.")
            return

    name = input("Enter Student Name: ").strip()
    try:
        marks = float(input("Enter Marks: "))
    except ValueError:
        print("Error: Marks must be a valid number.")
        return

    students.append({"Roll Number": roll, "Name": name, "Marks": str(marks)})
    save_students(students)
    print(f"Student '{name}' added and saved successfully!")

def search_student():
    students = load_students()
    roll = input("Enter Roll Number to search: ").strip()
    
    for student in students:
        if student["Roll Number"] == roll:
            print("\n--- Student Found ---")
            print(f"Roll Number : {student['Roll Number']}")
            print(f"Name        : {student['Name']}")
            print(f"Marks       : {student['Marks']}")
            return
            
    print(f"No student found with Roll Number '{roll}'.")

def delete_student():
    students = load_students()
    roll = input("Enter Roll Number to delete: ").strip()
    
    updated_students = [s for s in students if s["Roll Number"] != roll]
    
    if len(updated_students) < len(students):
        save_students(updated_students)
        print(f"Student with Roll Number {roll} deleted successfully!")
    else:
        print(f"No student found with Roll Number '{roll}'.")

def view_all_students():
    students = load_students()
    if not students:
        print("No student records found.")
    else:
        print("\n" + "="*40)
        print(f"{'Roll No':<10} | {'Name':<18} | {'Marks':<8}")
        print("="*40)
        for s in students:
            print(f"{s['Roll Number']:<10} | {s['Name']:<18} | {s['Marks']:<8}")
        print("="*40)

def main():
    initialize_csv()
    while True:
        print("\n=== STUDENT MANAGEMENT SYSTEM ===")
        print("1. Add Student")
        print("2. Search Student")
        print("3. Delete Student")
        print("4. View All Students")
        print("5. Exit")
        
        choice = input("Select an option (1-5): ").strip()
        
        if choice == '1':
            add_student()
        elif choice == '2':
            search_student()
        elif choice == '3':
            delete_student()
        elif choice == '4':
            view_all_students()
        elif choice == '5':
            print("Exiting Student Management System. Goodbye!")
            break
        else:
            print("Invalid selection! Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()