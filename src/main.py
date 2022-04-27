from fastapi import FastAPI

from cpf.controllers import cpf_controller
from names.controllers.names_controller import NamesControllerImpl
from people.controllers.people_controller import PeopleControllerImp

# API Object
app = FastAPI()


""" Routes """


@app.get("/")  # Returns a CPF AND a name
def get_people():

    people = PeopleControllerImp().get_people()
    cpf = cpf_controller.CPFControllerImp().return_a_valid_cpf()

    return {"People": [cpf, people], }


@app.get("/cpf")  # Returns a valid CPF
def get_cpf():
    cpf = cpf_controller.CPFControllerImp().return_a_valid_cpf()
    return {"CPF": f"{cpf}"}


@app.get("/name/male")  # Returns a male name
def get_name():
    name = NamesControllerImpl().get_name(gender="M")
    return {"Name": f"{name}"}


@app.get("/name/female")  # Returns a female name
def get_name():
    name = NamesControllerImpl().get_name(gender="F")
    return {"Name": f"{name}"}


@app.get("/password/{length}")
def get_password(length: int):
    pass
