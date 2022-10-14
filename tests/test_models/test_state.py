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

    def test_has_attributes(self):
        """Check attributes type """
        obj2 = State()
        self.assertTrue(hasattr(obj2, 'name'))
