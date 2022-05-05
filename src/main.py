from typing import Optional
from fastapi import FastAPI

from cpf.controllers import cpf_controller
from names.controllers.names_controller import NamesControllerImpl
from password.controllers.password_controller import PasswordControllerImp
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


@app.get("/password")  # Returns a password. Default length of 8
def get_password():
    password = PasswordControllerImp().get_password(length=8)
    return {"Password": f"{password}"}

@app.get("/password/{length}")  # Returns a password based in a choosed length
def get_password(length: Optional[int] = 8):
    password = PasswordControllerImp().get_password(length=length)
    return {"Password": f"{password}"}
