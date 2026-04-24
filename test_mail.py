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

    def test_incorrect_emails(self):
        incorrect_list = [
            "",
            "address",
            "@username.com",
            "oksana@.com",
            "polina@mail.",
            "user@mail,ru",
            "user@mail!.ru",
            "user name@gmail.com",
            "...@mail.ru",
            "a@gmail.com",
            "user@mail",
            "p1@"
        ]
        for email in incorrect_list:
            with self.subTest(email=email):
                self.assertFalse(is_valid_email(email))

if __name__ == '__main__':
    unittest.main()




