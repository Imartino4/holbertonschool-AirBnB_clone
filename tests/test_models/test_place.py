#!/usr/bin/python3
""" Unittest """

import unittest
from models.base_model import BaseModel
from models.place import Place

class TestPlace(unittest.TestCase):
    """ Tests on Place class"""

    def test_init(self):
        """Test when initialize a new object"""
        obj1 = Place()
        self.assertEqual(type(obj1.id), str)

    def test_attribute(self):
        """Test adding value an attribute"""
        obj2 = Place()
        obj2.name = "Parque Central"
        obj2.number_rooms = 30000
        for k, v in obj2.__dict__.items():
            if k == 'name':
                obj_val = v
        self.assertEqual(obj_val, 'Parque Central')
        self.assertTrue(type(obj2.number_rooms) == int)


