#!/usr/bin/python3
"""This is the module for the file_storage class"""

import json

class FileStorage:
    """This is the file_storage class"""
    
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        obj_class_name = obj.__class__.__name__ + "." + obj.id
        self.__objects[obj_class_name] = obj

    def save(self):
        with open(self.__file_path, 'w') as file:
            new_dict = {}
            for key, value in self.__objects.items():
                new_dict[key] = value.to_dict()
            json_string = json.dumps(new_dict)
            file.write(json_string)

    def reload(self):
        try:
            from models.base_model import BaseModel
            with open(self.__file_path, 'r') as file:
                json_string = file.read()
                new_dict = json.loads(json_string)
                for key, value in new_dict.items():
                    self.__objects[key] = BaseModel(**value)
        except:
            pass

