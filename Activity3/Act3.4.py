def read_student_file():
    try:
        with open("students.txt", "r") as file:
            print("\nStudent Information:")
            print("-"*50)
            
            for line in file:
                print(line.strip())
            print("-"*50)
    
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"Error reading file: {e}")

if __name__ == "__main__":
    read_student_file()