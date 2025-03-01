import unittest
from src.record_manager import load_records, save_records, add_record, edit_record, delete_record, show_all_students, order_by_last_name, order_by_grade

class TestRecordManager(unittest.TestCase):

    def setUp(self):
        self.records = [
            ('123456', ('John', 'Doe'), 85.0, 90.0),
            ('654321', ('Jane', 'Smith'), 75.0, 80.0)
        ]
        self.filename = 'test_students.json'
        self.test_records = [
            ("123456", ("John", "Doe"), 85.5, 90.0),
            ("234567", ("Jane", "Apple"), 90.0, 88.5),
            ("345678", ("Bob", "Brown"), 78.5, 82.0)
        ]

    def test_load_records(self):
        save_records(self.filename, self.records)
        loaded_records = load_records(self.filename)
        self.assertEqual(loaded_records, self.records)

    def test_save_records(self):
        new_records = [('111111', ('Alice', 'Johnson'), 88.0, 92.0)]
        save_records(self.filename, new_records)
        loaded_records = load_records(self.filename)
        self.assertEqual(loaded_records, new_records)

    def test_add_record(self):
        new_record = ('222222', ('Bob', 'Brown'), 78.0, 85.0)
        add_record(self.records, new_record)
        self.assertIn(new_record, self.records)

    def test_edit_record(self):
        edit_record(self.records, '123456', first_name='Johnny', last_name='Doe', class_standing=90.0, major_exam=95.0)
        self.assertEqual(self.records[0], ('123456', ('Johnny', 'Doe'), 90.0, 95.0))

    def test_delete_record(self):
        delete_record(self.records, '654321')
        self.assertNotIn(('654321', ('Jane', 'Smith'), 75.0, 80.0), self.records)

    def test_order_by_last_name(self):
        ordered = order_by_last_name(self.test_records)
        self.assertEqual(ordered[0][1][1], "Apple")
        self.assertEqual(ordered[1][1][1], "Brown")
        self.assertEqual(ordered[2][1][1], "Doe")

    def test_order_by_grade(self):
        ordered = order_by_grade(self.test_records)
        # Calculate expected final grades (60% class standing + 40% major exam)
        grades = [(0.6 * r[2] + 0.4 * r[3]) for r in self.test_records]
        self.assertEqual(ordered[0], self.test_records[1])  # Jane should be first
        self.assertEqual(ordered[1], self.test_records[0])  # John should be second
        self.assertEqual(ordered[2], self.test_records[2])  # Bob should be last

    def tearDown(self):
        import os
        if os.path.exists(self.filename):
            os.remove(self.filename)

if __name__ == '__main__':
    unittest.main()