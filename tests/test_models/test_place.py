#!/usr/bin/python3
""" Unittest """

import unittest
from models.place import Place

class TestBaseModel_Place(unittest.TestCase):
    """ Tests on Place class"""

    def test_place_name(self):
        """Tests for Place class"""
        place = Place()
        self.assertEqual(type(place.name), str)