#!/usr/bin/python3
""" Unittest """

import unittest
from models.base_model import BaseModel
from models import storage
import os


class TestFileStorage(unittest.TestCase):
    """ Test FileStorage class """

    def setUp(self):
        try:
            os.remove("file.json")
        except Exception:
            pass
        storage.reload()
        self.obj1 = BaseModel()
        self.obj2 = BaseModel()
        storage.save()

    def test_all(self):
        self.assertTrue(len(storage.all()) > 0)

    def test_new(self):
        obj = BaseModel()
        storage.new(obj)
        self.assertTrue(obj in storage.all().values())

if __name__ == '__main__':
    unittest.main()