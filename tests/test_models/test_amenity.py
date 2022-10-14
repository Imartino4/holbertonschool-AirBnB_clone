#!/usr/bin/python3
""" Unittest """

import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    """ Tests on Amenity class"""

    def test_has_attributes(self):
        """Check attributes type """
        obj2 = Amenity()
        self.assertEqual(type(obj2.name), str)
