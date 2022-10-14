#!/usr/bin/python3
""" Unittest """

import unittest
from models.city import City

class TestCity(unittest.TestCase):
    """ Tests on Place class"""

    def test_has_attributes(self):
        """Check attributes type """
        city = City()
        self.assertEqual(type(city.name), str)
