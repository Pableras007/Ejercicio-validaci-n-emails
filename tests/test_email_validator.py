import unittest
from emails.validator import EmailValidator

class TestEmailValidator(unittest.TestCase):
    def setUp(self):
        self.validator = EmailValidator()

    def test_valid_emails(self):
        valid_emails = [
            "usuario@example.com",
            "nombre.apellido@dominio.co",
            "user_name@sub.dominio.com",
            "user-name@dominio.org",
            "user.name+alias@dominio.net",
            "pablo@gmail.com"
        ]
        for correo in valid_emails:
            with self.subTest(correo=correo):
                self.assertTrue(self.validator.validar(correo))

    def test_invalid_emails(self):
        invalid_emails = [
            "usuarioexample.com",
            "usuario@.com",
            "usuario@com",
            "@dominio.com",
            "usuario@dominio",
            12345,
            None
        ]
        for correo in invalid_emails:
            with self.subTest(correo=correo):
                self.assertFalse(self.validator.validar(correo))

    def test_type_error(self):
        with self.assertRaises(TypeError):
            self.validator.validar(12345)

if __name__ == "__main__":
    unittest.main()
