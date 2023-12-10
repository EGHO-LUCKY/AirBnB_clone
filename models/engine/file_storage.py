#!/usr/bin/python3
"""This is the module for the file_storage class"""

import json

class FileStorage:
    """This is the file_storage class"""
    
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary of objects"""
        return self.__objects

    def new(self, obj):
        """Adds a new object to the object dictionary"""
        obj_class_name = obj.__class__.__name__ + "." + obj.id
        self.__objects[obj_class_name] = obj

    def save(self):
        """Saves the object dictionary to a file"""
        with open(self.__file_path, 'w', encoding="UTF-8") as file:
            new_dict = {}
            for key, value in self.__objects.items():
                new_dict[key] = value.to_dict()
            json.dump(new_dict, file)

    def reload(self):
        """Loads the file into the object dictionary"""
        try:
            from models.base_model import BaseModel
            with open(self.__file_path, 'r', encoding="UTF-8") as file:
                new_dict = json.load(file)
                for key, value in new_dict.items():
                    self.__objects[key] = BaseModel(**value)
                    print(BaseModel(**value))
        except FileNotFoundError:
            pass

