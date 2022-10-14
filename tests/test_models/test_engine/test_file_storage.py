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

    def test_save(self):
        try:
            os.remove("file.json")
        except Exception:
            pass
        storage.reload()
        obj1 = BaseModel()
        obj2 = BaseModel()
        storage.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_reload(self):
        objects1 = storage.all().copy()
        storage.reload()
        objects2 = storage.all().copy()
        self.assertEqual(len(objects1), len(objects2))

if __name__ == '__main__':
    unittest.main()
