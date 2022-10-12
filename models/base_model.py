#!/usr/bin/python3
""" This module contains the BaseModel class
    for AirBnB clone console """
import uuid
from datetime import datetime


class BaseModel():
    """ BaseModel class """

    def __init__(self, *args, **kwargs):
        """Constructor for BaseModel
            Public attributes:
                -id: unique number assigned to created instance
                -created_at: date and time when an the instance is created
                -updated_at: update date and time if the instance changes
        """
        if kwargs:
            for k, v in kwargs.items():
                if k != '__class__':
                    setattr(self, k, v)
                self.created_at = datetime.fromisoformat(kwargs['created_at'])
                self.updated_at = datetime.fromisoformat(kwargs['updated_at'])
        else:
            from models.__init__ import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """ __str__ method customized """
        return(f"[{__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """ Update the 'update_at' attribute with current datetime """
        from models.__init__ import storage
        self.updated_at = datetime.now()
        storage.save()


    def to_dict(self):
        """ Returns a dictionary containing all k/v of __dict__, 
            a key __class__ with corresponding value is added and
            the datetime format must be %Y-%m-%dT%H:%M:%S.%f """
        new_dict = self.__dict__.copy()
        for k, v in new_dict.items():
            if k == 'created_at':
                new_dict[k] = self.created_at.isoformat()
            if k == 'updated_at':
                new_dict[k] = self.updated_at.isoformat()
        new_dict['__class__'] = __class__.__name__
        return new_dict
