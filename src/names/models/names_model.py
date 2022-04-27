from dataclasses import dataclass
from random import Random
from typing import Protocol

from db import names


class NamesModel(Protocol):

    def generate_name(self, gender: str) -> None:
        """" Get a name from the tuple randomly"""

    def generate_last_name(self) -> None:
        """" Get a last name from the tuple randomly and concat with name """


@dataclass
class NamesModelImp(NamesModel):

    male = names.male_names
    female = names.female_names
    last_name = names.last_names
    name = ""
    

    def generate_name(self, gender: str) -> None:

        if gender == "M":
            index = Random().randint(0, len(self.male) - 1)
            self.name = self.male[index]
            self.generate_last_name()

        elif gender == "F":
            index = Random().randint(0, len(self.female) -1)
            self.name = self.female[index]
            self.generate_last_name()

    def generate_last_name(self):
        index = Random().randint(0, len(self.last_name) - 1)
        self.name = self.name + " " + self.last_name[index]
