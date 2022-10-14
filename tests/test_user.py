#!/usr/bin/python3
""" Unittest """

import unittest
from models.user import User

class TestUser(unittest.TestCase):
    """ Tests on BaseModel class"""

    def test_user_email(self):
        """ Check attributes type """
        user = User()
        self.assertTrue(hasattr(user.__class__, 'email'))

    def test_user_password(self):
        """ Check attributes type """
        user = User()
        self.assertTrue(hasattr(user.__class__, 'password'))

    def test_user_first_name(self):
        """ Check attributes type """
        user = User()
        self.assertTrue(hasattr(user.__class__, 'first_name'))

    def test_user_last_name(self):
        """ Check attributes type """
        user = User()
        self.assertTrue(hasattr(user.__class__, 'last_name'))
