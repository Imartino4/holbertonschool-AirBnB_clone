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
        obj1 = BaseModel()
        obj2 = BaseModel()
        storage.save()

    def test_all(self):
        amount = len(storage.all())
        self.assertTrue(amount > 0)

    def test_new(self):
        obj = BaseModel()
        storage.new(obj)
        self.assertTrue(obj in storage.all().values())

    def test_save_reload(self):
        try:
            os.remove("file.json")
        except Exception:
            pass
        storage.reload()
        obj1 = BaseModel()
        obj2 = BaseModel()
        storage.save()
        self.assertTrue(os.path.exists("file.json"))

if __name__ == '__main__':
    unittest.main()