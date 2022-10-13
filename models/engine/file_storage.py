#!/usr/bin/python3
""" This module contains FileStorage class """
import json
import os
from models.base_model import BaseModel
from models import user, state, city, amenity, place, review

classes = {'BaseModel': BaseModel, 'User': user.User, 'State': state.State, 'City': city.City,
        'Amenity': amenity.Amenity, 'Place': place.Place, 'Review': review.Review}

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
        self.__objects[name] = obj

    def save(self):
        """ This method serialize an object to JSON file"""
        with open(self.__file_path, 'w') as file:
            json_dict = {}
            for k, v in self.__objects.items():
                json_dict[k] = v.to_dict()
            file.write(json.dumps(json_dict))
    
    def reload(self):
        """ This method deserializes an Json file to an object """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                json_str = file.read()
                if len(json_str) > 0:
                    json_dict = json.loads(json_str)
                    self.__objects.clear()
                    for k, obj_dict in json_dict.items():
                        self.__objects[k] = classes[k[:-37]](**obj_dict)
