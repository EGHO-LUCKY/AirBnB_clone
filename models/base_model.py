#!/usr/bin/python3
"""This is the base model for the AirBnB project"""

import uuid
import datetime
from models import storage


class BaseModel:
    """This is the base class"""
    def __init__(self, *args, **kwargs):
        """Initializes the BaseModel class"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "created_at":
                    self.created_at = datetime.datetime.fromisoformat(value)
                elif key == "updated_at":
                    self.updated_at = datetime.datetime.fromisoformat(value)
                elif key == "__class__":
                    pass
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self)

    def __str__(self):
        """This is the string representation of the BaseModel class"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """The Save function saves the data in the database"""
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary representation of the BaseModel class"""
        my_dict = {"__class__": self.__class__.__name__}
        search_list = ["created_at", "updated_at"]
        for key, value in self.__dict__.items():
            if key in search_list:
                value = value.isoformat()
            my_dict[key] = value
        return my_dict
