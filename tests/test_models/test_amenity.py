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

    def test_has_attributes(self):
        """Check attributes type """
        obj2 = Amenity()
        self.assertTrue(hasattr(obj2, 'name'))
