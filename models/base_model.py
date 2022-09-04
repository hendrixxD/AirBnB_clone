#!/usr/bin/python3
"""BaseModel that defines all common attributes/methods
to be used for other classses"""


from datetime import datetime
import uuid
import models


class BaseModel:
    """BaseModel class"""

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key = "created_at" or key = "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
                else:
                    self.id = str(uuid.uuid4())
                    self.created_at = self.updated_at = datetime.now()

    def save(self):
        """updates the public instance attribute
        updated_at: with the current datetime
        """
        self.update = datetime.now()
        models.storage.save()

    def __str__(self):
        """ String """
        return('[' + type(self).__name__ + '] (' + str(self.id) +
               ') ' + str(self.__dict__))

    def to_dict(self):
        """
        Method to return a dict containing all key/value of __dict__
        instance
        """
        dic = dict(**self.__dict__)
        dic['__class__'] = str(type(self).__name__)
        dic['created_at'] = self.created_at.isoformat()
        dic['updated_at'] = self.updated_at.isoformat()

        return (dic)
