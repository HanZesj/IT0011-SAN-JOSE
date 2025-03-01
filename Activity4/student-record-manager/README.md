# File: /student-record-manager/student-record-manager/README.md

# Student Record Manager

This project is a Python application for managing student records. Each record consists of a six-digit Student ID, a tuple for the Student Name (first name and last name), the Student Class Standing grade, and the Major Exam grade. The application provides a menu-driven interface to perform various operations on student records.

## Features

- Open a file to load student records.
- Save the current records to a file.
- Save the records as a new file.
- Show all student records.
- Order records by last name.
- Order records by grade (calculated as 60% of Class Standing and 40% of Major Exam).
- Show a specific student record.
- Add a new student record.
- Edit an existing student record.
- Delete a student record.

## Project Structure

```
student-record-manager
├── src
│   ├── __init__.py
│   ├── main.py
│   ├── record_manager.py
│   └── utils
│       ├── __init__.py
│       ├── file_handler.py
│       └── validators.py
├── data
│   └── students.json
├── tests
│   ├── __init__.py
│   ├── test_record_manager.py
│   └── test_validators.py
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd student-record-manager
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the application, execute the following command:
```
python src/main.py
```

Follow the on-screen instructions to manage student records.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License.