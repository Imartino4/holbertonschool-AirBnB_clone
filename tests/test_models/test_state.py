#!/usr/bin/python3
""" Unittest """

import unittest
from models.base_model import BaseModel
from models.state import State

class TestState(unittest.TestCase):
    """ Tests on State class"""

    def test_init(self):
        """Test when initialize a new object"""
        obj1 = State()
        self.assertEqual(type(obj1.id), str)

    def test_attribute(self):
        """Test adding value an attribute"""
        obj2 = State()
        obj2.name = "Montevideo"
        for k, v in obj2.__dict__.items():
            if k == 'name':
                obj_val = v
        self.assertEqual(obj_val, 'Montevideo')

