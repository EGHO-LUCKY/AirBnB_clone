#!/usr/bin/python3
"""This is the module for the HBNBCommand console class"""

import cmd
from models.base_model import BaseModel
import json
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def read_json(self, file_path):
        try:
            with open(file_path, "r", encoding="UTF-8") as file:
                new_dict = json.load(file)
                return new_dict
        except:
            return None

    def write_json(self, file_path, new_dict):
        try:
            with open(file_path, "w", encoding="UTF-8") as file:
                json.dump(new_dict, file)
        except:
            print("There is no data in the data base")

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
        if arg == "BaseModel":
            new_instance = BaseModel()
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
            if my_list[0] != "BaseModel":
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")
        elif count == 2:
            new_dict = self.read_json("file.json")
            key = ".".join(my_list)
            if new_dict is not None:
                if key in new_dict.keys():
                    print(BaseModel(**new_dict[key]))
                else:
                    print("** no instance found **")
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
            if my_list[0] != "BaseModel":
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")
        elif count == 2:
            with open("file.json", "r") as file:
                new_dict = json.load(file)
                key = ".".join(my_list)
                if key in new_dict.keys():
                    del new_dict[key]
                else:
                    print("** no instance found **")
            with open("file.json", "w") as file:
                json.dump(new_dict, file)

    def do_all(self, arg):
        """Displays all models in the database"""
        if not arg:
            try:
                new_list = []
                new_dict = self.read_json("file.json")
                for key, value in new_dict.items():
                    new_list.append(str(BaseModel(**new_dict[key])))
                #new_list = [str(BaseModel(**value)) for value in new_dict.values()]
                if new_list:
                    print(new_list)
                else:
                    print("There is no data in the data base")
            except:
                print("There is no data in the data base")
        else:
            model_dict = {"BaseModel": BaseModel}
            new_dict = self.read_json("file.json")
            new_list = []
            if new_dict is not None:
                for key, value in new_dict.items():
                    my_list = key.split(".")
                    if my_list[0] == arg:
                        new_list.append(str(model_dict[arg](**value)))
            if not new_list:
                print("** class doesn't exist **")
            else:
                print(new_list)

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
            if my_list[0] == "BaseModel":
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
                print("There is no data in the data base")
            else:
                if key in all_instance.keys():
                    try:
                        value = my_list[3].split('"')[1]
                    except:
                        value = my_list[3]
                    attribute = my_list[2]
                    instance = all_instance[key]
                    setattr(instance, attribute, value)
                    instance.save()

if __name__ == "__main__":
    HBNBCommand().cmdloop()
































