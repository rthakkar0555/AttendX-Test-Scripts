import unittest


def login(username, password):
    if username == "student" and password == "attend123":
        return "Login successful"
    return "Invalid credentials"


class LoginTest(unittest.TestCase):

    def test_valid_login(self):
        self.assertEqual(
            login("student", "attend123"),
            "Login successful"
        )

    def test_invalid_password(self):
        self.assertEqual(
            login("student", "wrong"),
            "Invalid credentials"
        )

    def test_invalid_username(self):
        self.assertEqual(
            login("unknown", "attend123"),
            "Invalid credentials"
        )

    def test_empty_username(self):
        self.assertEqual(
            login("", "attend123"),
            "Invalid credentials"
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)