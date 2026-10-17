import unittest


def mark_attendance(student_id, status):
    if not student_id:
        return "Invalid student ID"

    if status not in ("Present", "Absent"):
        return "Invalid attendance status"

    return f"{student_id}: {status}"


class AttendanceMarkingTest(unittest.TestCase):

    def test_mark_present(self):
        self.assertEqual(
            mark_attendance("STU101", "Present"),
            "STU101: Present"
        )

    def test_mark_absent(self):
        self.assertEqual(
            mark_attendance("STU102", "Absent"),
            "STU102: Absent"
        )

    def test_invalid_student_id(self):
        self.assertEqual(
            mark_attendance("", "Present"),
            "Invalid student ID"
        )

    def test_invalid_status(self):
        self.assertEqual(
            mark_attendance("STU103", "Late"),
            "Invalid attendance status"
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)