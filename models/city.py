#!/usr/bin/python3
""" This module contains the User class """
from models.base_model import BaseModel


class City(BaseModel):
    """ Class representing City """

    state_id = ""
    name = ""
