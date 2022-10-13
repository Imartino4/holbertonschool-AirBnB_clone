#!/usr/bin/python3
""" This module contains the User class """
from models.base_model import BaseModel


class User(BaseModel):
    """ User class """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
