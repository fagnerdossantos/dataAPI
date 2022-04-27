from ast import Str
from dataclasses import dataclass
from random import Random
from typing import Protocol

from names.controllers.names_controller import NamesController, NamesControllerImpl

class PeopleModel(Protocol):
    def generate_people() -> None:
        """ Generates a CPF an a name"""

@dataclass
class PeopleModelImp():

    names = NamesControllerImpl()
    
    gender = ("M", "F")
    people = ""

    def generate_people(self) -> None:
        index = Random().randint(0, 1)
        self.people = self.names.get_name(gender=self.gender[index])
