#!/usr/bin/env python3
""" Defines a base class for all the modules. """

import uuid
from datetime import datetime


class BaseModel:
    """ A base class that other class inherit from """

    def __int__(self, *args, **kwargs):
        """initialize instance of class.

            Args:
                args - positional argument
                kwargs - ketword argument
        """
        if (kwargs):
            ft = "%Y-%m-%dT%H:%M:%S.%f"

            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, ft)
                elif key != "__class__":
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """ print [<classname>] (<self.id>) <self.__dict__> """

        return f"[{self.__class__.name}] ({self.id}) {self.__dict__}"

    def save(self):
        """ update_at with the current datetime """

        updated_at = datetime.now()

    def to_dict(self):
        """ returns a dictionary cantaining all key-value of __dict_
        of the instance """

        dictionary = self.__dict__.copy()
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        dictionary["__class__"] = self.__class__.__name__

        return (dictionary)
