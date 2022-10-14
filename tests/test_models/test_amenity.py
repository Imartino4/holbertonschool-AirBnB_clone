#!/usr/bin/python3
""" Unittest """

import unittest
from models.base_model import BaseModel
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    """ Tests on Amenity class"""

    def test_init(self):
        """Test when initialize a new object"""
        obj1 = Amenity()
        self.assertEqual(type(obj1.id), str)

    def test_attribute(self):
        """Test adding value an attribute"""
        obj2 = Amenity()
        obj2.name = "Spa"
        for k, v in obj2.__dict__.items():
            if k == 'name':
                obj_val = v
        self.assertEqual(obj_val, 'Spa')

