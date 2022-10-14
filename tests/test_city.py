#!/usr/bin/python3
""" Unittest """

import unittest
from models.base_model import BaseModel
from models.city import City

class TestCity(unittest.TestCase):
    """ Tests on Place class"""

    def test_init(self):
        """Test when initialize a new object"""
        obj1 = City()
        self.assertEqual(type(obj1.id), str)

    def test_has_attributes(self):
        """Check attributes type """
        obj2 = City()
        self.assertTrue(hasattr(obj2, 'state_id'))
        self.assertTrue(hasattr(obj2, 'name'))
