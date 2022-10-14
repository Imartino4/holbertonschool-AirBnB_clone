#!/usr/bin/python3
""" Unittest """

import unittest
from models.user import User

class TestUser(unittest.TestCase):
    """ Tests on BaseModel class"""

    def test_user_email(self):
        """ Check attributes type """
        user = User()
        self.assertEqual(type(user.email), str)

    def test_user_first_name(self):
        """ Check attributes type """
        user = User()
        self.assertEqual(type(user.first_name), str)

    def test_user_last_name(self):
        """ Check attributes type """
        user = User()
        self.assertEqual(type(user.last_name), str)

    def test_user_password(self):
        """ Check attributes type """
        user = User()
        self.assertEqual(type(user.password), str)
