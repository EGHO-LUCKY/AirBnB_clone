#!/usr/bin/python3
"""This is the module for the HBNBCommand console class"""

import cmd

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

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

if __name__ == "__main__":
    HBNBCommand().cmdloop()