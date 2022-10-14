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

    def test_attribute(self):
        """Test adding value an attribute"""
        obj2 = Review()
        obj2.text = "Everything good"
        for k, v in obj2.__dict__.items():
            if k == 'text':
                obj_val = v
        self.assertEqual(obj_val, 'Everything good')

