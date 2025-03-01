def get_student_info():
    """Get student information from user input"""
    last_name = input("Enter last name: ")
    first_name = input("Enter first name: ")
    age = input("Enter age: ")
    contact = input("Enter contact number: ")
    course = input("Enter course: ")
    return last_name, first_name, age, contact, course

def format_student_info(last_name, first_name, age, contact, course):
    """Format student information into a string"""
    return f"Name: {last_name}, {first_name}\nAge: {age}\nContact: {contact}\nCourse: {course}\n{'-'*50}\n"

def save_to_file(student_info):
    """Save formatted student information to students.txt"""
    try:
        with open("students.txt", "a") as file:
            file.write(student_info)
        return True
    except Exception as e:
        print(f"Error saving to file: {e}")
        return False

def main():
    # Get student information
    last_name, first_name, age, contact, course = get_student_info()
    
    # Format the information
    formatted_info = format_student_info(last_name, first_name, age, contact, course)
    
    # Save to file
    if save_to_file(formatted_info):
        print("\nStudent information has been successfully saved to students.txt!")
    else:
        print("\nFailed to save student information.")

if __name__ == "__main__":
    main() 