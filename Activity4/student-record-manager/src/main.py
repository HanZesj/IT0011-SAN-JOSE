import json
import os
from record_manager import load_records, save_records, show_all_students, order_by_last_name, order_by_grade, show_student_record, add_record, edit_record, delete_record

def main():
    filename = "data/students.json"
    records = load_records(filename)
    
    while True:
        print("\nMenu:")
        print("1. Show All Students Record")
        print("2. Order by Last Name")
        print("3. Order by Grade")
        print("4. Show Student Record")
        print("5. Add Record")
        print("6. Edit Record")
        print("7. Delete Record")
        print("8. Save File")
        print("9. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            show_all_students(records)
        elif choice == '2':
            records = order_by_last_name(records)
            show_all_students(records)
        elif choice == '3':
            records = order_by_grade(records)
            show_all_students(records)
        elif choice == '4':
            student_id = input("Enter Student ID: ")
            show_student_record(records, student_id)
        elif choice == '5':
            add_record(records)
        elif choice == '6':
            edit_record(records)
        elif choice == '7':
            delete_record(records)
        elif choice == '8':
            save_records(filename, records)
            print("Records saved successfully!")
        elif choice == '9':
            save_records(filename, records)
            print("Exiting and saving records...")
            break
        else:
            print("Invalid choice. Please enter a number between 1-9.")

if __name__ == "__main__":
    main()