#!/usr/bin/python3
""" Unittest """

import unittest
from models.base_model import BaseModel
import datetime
import time
import os


class TestBase(unittest.TestCase):
    """ Tests on BaseModel class"""

    def test_init(self):
        """Test when initialize a new object"""
        obj1 = BaseModel()
        self.assertEqual(type(obj1.id), str)
        self.assertEqual(type(obj1.created_at), datetime.datetime)

    def test_str_meth(self):
        """ Test on str method """
        obj2 = BaseModel()
        output = f"[{obj2.__class__.__name__}] ({obj2.id}) {obj2.__dict__}"
        self.assertEqual(obj2.__str__(), output)

    def test_to_dict(self):
        """ Test on to_dict method """
        dict_out = {
                "id": "1",
                "created_at": "2022-10-13T14:24:35.191100",
                "updated_at": "2022-10-13T14:24:35.191100",
                "__class__": "BaseModel"
                }
        obj3 = BaseModel(**dict_out)
        self.assertEqual(obj3.to_dict(), dict_out)

    def test_save(self):
        obj4 = BaseModel()
        try:
            os.remove("file.json")
        except Exception:
            pass
        updated = str(obj4.updated_at)
        time.sleep(2)
        obj4.save()
        self.assertNotEqual(updated, obj4.updated_at)
        self.assertTrue(os.path.exists("file.json"))

if __name__ == '__main__':
    unittest.main()
