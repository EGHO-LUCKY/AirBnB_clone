#!/usr/bin/python3
"""This is the module for the HBNBCommand console class"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import json
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    model_dict = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
            }

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """Handles end-of-file (Ctrl+D or Ctrl+Z).
        """
        print("")
        return True

    def emptyline(self):
        pass

    def do_create(self, arg):
        """creates a Model class"""
        if arg in self.model_dict:
            new_instance = self.model_dict[arg]()
            new_instance.save()
            print(new_instance.id)
        elif not arg:
            print("** class name missing **")
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Displays a model with an id value"""
        if arg:
            my_list = arg.split(" ")
            count = len(my_list)
        else:
            count = 0

        if count == 0:
            print("** class name missing **")
        elif count == 1:
            if my_list[0] in self.model_dict:
                print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        elif count == 2:
            key = ".".join(my_list)
            all_instances = storage.all()
            if key in all_instances.keys():
                instance = all_instances[key]
                print(instance)
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes a model from the database"""
        if arg:
            my_list = arg.split(" ")
            count = len(my_list)
        else:
            count = 0

        if count == 0:
            print("** class name missing **")
        elif count == 1:
            if my_list[0] in self.model_dict:
                print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        elif count == 2:
            all_instances = storage.all()
            key = ".".join(my_list)
            if key in all_instances.keys():
                del all_instances[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Displays all models in the database"""
        if not arg:
            try:
                all_instances = storage.all()
                new_list = [str(value) for value in all_instances.values()]
                print(new_list)
            except Exception:
                print("[]")
        else:
            all_instances = storage.all()

            new_list = []
            if all_instances is not None:
                for key, value in all_instances.items():
                    my_list = key.split(".")
                    if my_list[0] == arg:
                        new_list.append(str(value))
                if not new_list:
                    print("** class doesn't exist **")
                else:
                    print(new_list)
            else:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates a Model in the database"""
        all_instance = storage.all()
        if arg:
            my_list = arg.split(" ")
            count = len(my_list)
        else:
            count = 0

        if count == 0:
            print("** class name missing **")
        elif count == 1:
            if my_list[0] in self.model_dict:
                print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        elif count == 2:
            key = ".".join(my_list)
            if all_instance is not None:
                if key in all_instance.keys():
                    print("** attribute name missing **")
                else:
                    print("** no instance found **")
            else:
                print("There is no data in the data base")
        elif count == 3:
            key = ".".join(my_list[:2])
            if all_instance is not None:
                if key in all_instance.keys():
                    print("** value missing **")
        else:
            key = ".".join(my_list[:2])
            if all_instance is None:
                pass
            else:
                if key in all_instance.keys():
                    try:
                        value = my_list[3].split('"')[1]
                    except Exception:
                        value = my_list[3]
                    attribute = my_list[2]
                    instance = all_instance[key]
                    setattr(instance, attribute, value)
                    instance.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
