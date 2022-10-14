#!/usr/bin/python3
""" Unittest """

import unittest
from models.review import Review

class TestReview(unittest.TestCase):
    """ Tests on Review class"""

    def test_has_attributes(self):
        """Check attributes type """
        review = Review()
        self.assertEqual(type(review.text), str)
