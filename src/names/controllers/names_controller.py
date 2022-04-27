from dataclasses import dataclass
from typing import Protocol

from names.models.names_model import NamesModelImp


class NamesController(Protocol):
    def get_name(self):
        """ Get the generated name """

    def get_last_name(self):
        """ Get the generated last name """


@dataclass
class NamesControllerImpl(NamesController):

    names_model = NamesModelImp()

    def get_name(self, gender: str):
        self.names_model.generate_name(gender=gender)
        return self.names_model.name

    def get_last_name(self):
        self.names_model.generate_last_name()
        return self.names_model.last
