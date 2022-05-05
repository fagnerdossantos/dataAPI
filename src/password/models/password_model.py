from dataclasses import dataclass
from random import Random
from typing import Protocol

from db.characters import characters_tuple


class PasswordModel(Protocol):
    def generate_password():
        """ Generates a password based in a user length choose or a defaut value """
    pass

@dataclass
class PasswordModelImp(PasswordModel):

    password = []
    characters = characters_tuple
    index = int
    
    def generate_password(self, length: int) -> None:
        
        self.password = []
        self.password.clear()

        for _ in range(length):
          self.index = Random().randint(a=0, b=len(self.characters) -1)
          self.password.append(self.characters[self.index])
