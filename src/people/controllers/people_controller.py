from dataclasses import dataclass
from typing import Protocol

from people.models.people_model import PeopleModelImp

class PeopleController(Protocol):
    def get_people() -> str:
        """ Get a CPF and name"""

@dataclass
class PeopleControllerImp(PeopleController):

    people_model = PeopleModelImp()

    def get_people(self) -> str:
        self.people_model.generate_people()
        return self.people_model.people
