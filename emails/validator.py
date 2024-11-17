
## TODO Gestión de excepciones
import re
import logging

class EmailValidator:
    def __init__(self):
        # Regex mejorado para validar correos electrónicos
        self.regex = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")

    def validar(self, correo: str):
        if not isinstance(correo, str):
            raise TypeError("El correo debe ser una cadena de texto.")

        try:
            return bool(re.fullmatch(self.regex, correo))
        except Exception as e:
            logging.error(f"Error al validar el correo '{correo}': {e}")
            return False

# Configuración del logging
logging.basicConfig(
    filename='email_validation.log',
    level=logging.ERROR,
    format='%(asctime)s:%(levelname)s:%(message)s'
)
