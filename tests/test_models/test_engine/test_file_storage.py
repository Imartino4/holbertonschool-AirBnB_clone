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
        storage.__objects.clear()
        self.obj1 = BaseModel()
        self.obj2 = BaseModel()
        storage.save()

    def test_all(self):
        amount_objs = len(storage.all())
        self.assertEqual(amount_objs, 2)

    def test_new(self):
        obj = BaseModel()
        storage.new(obj)
        self.assertTrue(obj in storage.all().values())