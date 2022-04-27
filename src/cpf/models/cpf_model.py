from dataclasses import dataclass
import random
from typing import Protocol


class CPFModel(Protocol):
    def seed() -> None:
        """ SEED CPF With random Numbers """
    def verify_digit() -> None:
        """ Calculate CPF digits """


@dataclass
class CPFModelImp(CPFModel):

    cpf = []

    # Seed teh CPF with 9 random number, from 0 to 9.
    def seed_cpf(self) -> None:

        # Cleaning the list
        self.cpf.clear()

        for _ in range(9):
            self.cpf.append(random.randint(0, 9))

    # Calculate the CPF digits
    def verify_digit(self, weight: int, sum=0) -> None:

        for value in self.cpf:
            sum += (value * weight)
            weight -= 1

        self.cpf.append(11 - (sum % 11) if sum % 11 >= 2 else 0)
