#!/usr/bin/python3
""" Unittest """

import unittest
from models.base_model import BaseModel
from models.user import User

class TestUser(unittest.TestCase):
    """ Tests on BaseModel class"""

    def test_init(self):
        """Test when initialize a new object"""
        obj1 = User()
        self.assertEqual(type(obj1.id), str)

    def test_user_email(self):
        """Check attributes type """
        obj2 = User()
        self.assertTrue(hasattr(obj2, 'email'))
        self.assertTrue(hasattr(obj2, 'password'))
        self.assertTrue(hasattr(obj2, 'first_name'))
        self.assertTrue(hasattr(obj2, 'last_name'))
