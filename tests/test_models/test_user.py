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
