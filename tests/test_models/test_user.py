#!/usr/bin/python3
""" Unittest """

import unittest
from models.base_model import BaseModel
from models.user import User
import datetime, time, os

class TestUser(unittest.TestCase):
    """ Tests on BaseModel class"""

    def test_init(self):
        """Test when initialize a new object"""
        obj1 = User()
        self.assertEqual(type(obj1.id), str)

    def test_attribute(self):
        """Test adding value an attribute"""
        obj1 = User()
        obj1.email = "hola@hbnb.com"
        for k, v in obj1.__dict__.items():
            if k == 'email':
                obj_val = v
        self.assertEqual(obj_val, 'hola@hbnb.com')


