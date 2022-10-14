#!/usr/bin/python3
""" Unittest """

import unittest
from models.base_model import BaseModel
from models.user import User

class TestUser(unittest.TestCase):
    """ Tests on BaseModel class"""

    def test_user_email(self):
        """Check attributes type """
        obj2 = User()
        self.assertTrue(hasattr(obj2, 'email'))
