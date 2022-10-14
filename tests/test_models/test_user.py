#!/usr/bin/python3
""" Unittest """

import unittest
from models.user import User

class TestUser(unittest.TestCase):
    """ Tests on BaseModel class"""

    def test_user(self):
        """ Check attribute type """
        user = User()
        self.assertEqual(type(user.password), str)
