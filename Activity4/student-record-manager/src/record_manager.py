import json
import os

def load_records(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return []

def save_records(filename, records):
    with open(filename, 'w') as file:
        json.dump(records, file, indent=4)

def show_all_students(records):
    print("\nAll Student Records:")
    for record in records:
        print(record)

def order_by_last_name(records):
    return sorted(records, key=lambda x: x[1][1])

def order_by_grade(records):
    return sorted(records, key=lambda x: (0.6 * x[2] + 0.4 * x[3]), reverse=True)

def show_student_record(records, student_id):
    for record in records:
        if record[0] == student_id:
            print("\nStudent Record Found:", record)
            return
    print("Student ID not found.")

def add_record(records):
    student_id = input("Enter Student ID (6-digit number): ")
    if not student_id.isdigit() or len(student_id) != 6:
        print("Invalid Student ID.")
        return
    
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    class_standing = float(input("Enter Class Standing Grade: "))
    major_exam = float(input("Enter Major Exam Grade: "))
    
    records.append((student_id, (first_name, last_name), class_standing, major_exam))
    print("Record Added Successfully!")

def edit_record(records):
    student_id = input("Enter Student ID to Edit: ")
    for i, record in enumerate(records):
        if record[0] == student_id:
            first_name = input("Enter New First Name: ")
            last_name = input("Enter New Last Name: ")
            class_standing = float(input("Enter New Class Standing Grade: "))
            major_exam = float(input("Enter New Major Exam Grade: "))
            
            records[i] = (student_id, (first_name, last_name), class_standing, major_exam)
            print("Record Updated Successfully!")
            return
    print("Student ID not found.")

def delete_record(records):
    student_id = input("Enter Student ID to Delete: ")
    for record in records:
        if record[0] == student_id:
            records.remove(record)
            print("Record Deleted Successfully!")
            return
    print("Student ID not found.")