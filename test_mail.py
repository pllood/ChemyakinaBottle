import unittest
from myform_mail import is_valid_email

class TestEmail(unittest.TestCase):
    def test_correct_emails(self):
        correct_list = [
            "user@example.com",
            "first@mail.ru",
            "name@gmail.com",
            "12345@site.ru",
            "admin@mail.org",
            "o.o@mail.ru"
        ]
        for email in correct_list:
            with self.subTest(email=email):
                self.assertTrue(is_valid_email(email))

    

if __name__ == '__main__':
    unittest.main()




