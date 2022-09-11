#!/usr/bin/python3
<<<<<<< HEAD
""" BaseModel """
from datetime import datetime
from uuid import uuid4

class BaseModel:
    """ const """

    def __init__(self, *args, **kwargs):
        """ Const """
        if kwargs:
=======
"""BaseModel that defines all common attributes/methods
to be used for other classses"""


from datetime import datetime
import uuid
import models


class BaseModel:
    """BaseModel class"""

    def __init__(self, *args, **kwargs):
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            models.storage.new(self)
        else:
>>>>>>> 83a05abaea3de27d5aa92904724a6c056ca30d1b
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
<<<<<<< HEAD
                if 'id' not in kwargs.keys():
                    self.id = str(uuid4())
                if 'created_at' not in kwargs.keys():
                    self.created_at = datetime.now()
                if 'updated_at' not in kwargs.keys():
                    self.updated_at = datetime.now()
                setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """ string """
        return('[' + type(self).__name__ + '] (' + str(self.id) +
               ') ' + str(self.__dict__))

    def save(self):
        """ saving """
=======
                if key != "__class__":
                    setattr(self, key, value)

    def save(self):
        """updates the public instance attribute
        updated_at: with the current datetime
        """
>>>>>>> 83a05abaea3de27d5aa92904724a6c056ca30d1b
        self.updated_at = datetime.now()
        models.storage.save()

    def __str__(self) -> str:
        """String"""
        _class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(_class_name, self.id, self.__dict__)

    def to_dict(self):
<<<<<<< HEAD
        """ dictonaries """
        aux_dict = self.__dict__.copy()
        aux_dict['__class__'] = self.__class__.__name__
        aux_dict['created_at'] = self.created_at.isoformat()
        aux_dict['updated_at'] = self.updated_at.isoformat()
        return aux_dict
=======
        """
        Method to return a dict containing all key/value of __dict__
        instance
        """
        dic = dict(**self.__dict__)
        dic['__class__'] = str(type(self).__name__)
        dic['created_at'] = self.created_at.isoformat()
        dic['updated_at'] = self.updated_at.isoformat()

        return (dic)
>>>>>>> 83a05abaea3de27d5aa92904724a6c056ca30d1b
