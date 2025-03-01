import unittest
from src.utils.validators import validate_student_id, validate_name, validate_grade

class TestValidators(unittest.TestCase):
    def test_validate_student_id(self):
        self.assertTrue(validate_student_id("123456"))
        self.assertFalse(validate_student_id("12345"))
        self.assertFalse(validate_student_id("1234567"))
        self.assertFalse(validate_student_id("abcdef"))

    def test_validate_name(self):
        self.assertTrue(validate_name("John"))
        self.assertTrue(validate_name("John Doe"))
        self.assertFalse(validate_name(""))
        self.assertFalse(validate_name("John123"))

    def test_validate_grade(self):
        self.assertTrue(validate_grade("85.5"))
        self.assertTrue(validate_grade("100"))
        self.assertTrue(validate_grade("0"))
        self.assertFalse(validate_grade("-1"))
        self.assertFalse(validate_grade("101"))
        self.assertFalse(validate_grade("abc"))

if __name__ == '__main__':
    unittest.main()