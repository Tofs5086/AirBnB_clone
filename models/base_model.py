#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime

import time
class BaseModel:
    """
    This is the base class
    """

    def __init__(self, id):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

        print("from init method, created_at:", type(self.created_at))
        print("from init method, updated at:", type(self.updated_at))

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    """return public instance method"""
    def save(self):
        self.updated_at = datetime.now()

    """ for serialization"""
    def to_dict(self):
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()

        print("from to_dict method created at:", type(obj_dict['created_at']))
        print("from to_dict method updated at:", type(obj_dict['updated_at']))
        return obj_dict
