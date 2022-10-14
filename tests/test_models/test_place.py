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

    def test_has_attributes(self):
        """Check attributes type """
        obj2 = Place()
        self.assertTrue(hasattr(obj2, 'city_id'))
        self.assertTrue(hasattr(obj2, 'user_id'))
        self.assertTrue(hasattr(obj2, 'name'))
        self.assertTrue(hasattr(obj2, 'description'))
        self.assertTrue(hasattr(obj2, 'number_rooms'))
        self.assertTrue(hasattr(obj2, 'number_bathrooms'))
        self.assertTrue(hasattr(obj2, 'max_guest'))
        self.assertTrue(hasattr(obj2, 'price_by_night'))
        self.assertTrue(hasattr(obj2, 'latitude'))
        self.assertTrue(hasattr(obj2, 'longitude'))
        self.assertTrue(hasattr(obj2, 'amenity_ids'))
