#!/usr/bin/python3
""" This module contains FileStorage class """
import json
import os


class FileStorage():
    """ FileStorage class"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ This method returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """ This method update __objects """
        name = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[name] = obj

    def save(self):
        """ This method serialize an object to JSON file"""
        with open(self.__file_path, 'w') as file:
            file.write(json.dumps(self.__objects))

    def reload(self):
        """ This method deserializes an Json file to an object """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                self.__objects = json.loads(file.read())
