def validate_student_id(student_id):
    """Validate that the student ID is a 6-digit number."""
    return student_id.isdigit() and len(student_id) == 6

def validate_name(name):
    """Validate that the name is not empty and contains only letters."""
    return bool(name) and all(c.isalpha() or c.isspace() for c in name)

def validate_grade(grade):
    """Validate that the grade is a number between 0 and 100."""
    try:
        grade_float = float(grade)
        return 0 <= grade_float <= 100
    except ValueError:
        return False