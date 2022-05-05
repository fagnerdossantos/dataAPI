from dataclasses import dataclass
from typing import Protocol

from password.models.password_model import PasswordModelImp


class PasswordController(Protocol):
    def get_password():
        """ Returns a random generated password """
    
    def format_password():
        """ Formats the password """


@dataclass
class PasswordControllerImp(PasswordController):

    model = PasswordModelImp()

    def get_password(self, length: int):

        self.model.generate_password(length=length)

        self.format_password()

        return self.model.password

    def format_password(self):
        password = str(self.model.password).replace(", ","").strip("[]")
        password = password.replace("'", "")
        self.model.password = password
