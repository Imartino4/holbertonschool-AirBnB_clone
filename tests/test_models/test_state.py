#!/usr/bin/python3
""" Unittest """

import unittest
from models.base_model import BaseModel
from models.state import State

class TestState(unittest.TestCase):
    """ Tests on State class"""

    def test_has_attributes(self):
        """Check attributes type """
        state = State()
        self.assertEqual(type(state.name), str)
