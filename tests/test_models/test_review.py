#!/usr/bin/python3
""" Unittest """

import unittest
from models.base_model import BaseModel
from models.review import Review

class TestPlace(unittest.TestCase):
    """ Tests on Review class"""

    def test_init(self):
        """Test when initialize a new object"""
        obj1 = Review()
        self.assertEqual(type(obj1.id), str)

    def test_has_attributes(self):
        """Check attributes type """
        obj2 = Review()
        self.assertTrue(hasattr(obj2, 'text'))
        self.assertTrue(hasattr(obj2, 'user_id'))
        self.assertTrue(hasattr(obj2, 'place_id'))
