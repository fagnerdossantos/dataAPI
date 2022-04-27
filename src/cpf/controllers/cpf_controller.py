from dataclasses import dataclass
from typing import Protocol

from cpf.models import cpf_model

class CPFController(Protocol):
    def return_a_valid_cpf() -> None:
        """ Returns a valid CPF number """
        

@dataclass
class CPFControllerImp(CPFController):

    # Instance
    cpf_model = cpf_model.CPFModelImp()

    # Return a valid CPF
    def return_a_valid_cpf(self) -> str:

        # Seed the CPF
        self.cpf_model.seed_cpf()

        # Generate cpf digits
        self.cpf_model.verify_digit(10)
        self.cpf_model.verify_digit(11)

        cpf = str(self.cpf_model.cpf).replace(", ", "").strip("[]")

        # Return a valid cpf
        return cpf
