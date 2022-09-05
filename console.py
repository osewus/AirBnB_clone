#!/usr/bin/python3
"""
Module contains command line interpreter
for managing Airbnb
"""
import cmd
import models
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    class HBNBCommand that inherits from Cmd class
    """
    prompt = "(hbnb) "
    classes = ['BaseModel']
    def do_all(self, arg):
        """
        All command to Prints all string representation of all instances
        based or not on the class name.
        Usage: all <Class_Name>  OR  all
        """
        pass

    def do_destroy(self, arg):
        """
        Destroy command to Deletes an instance based on the class name and id
        Usage: destroy <Class_Name> <obj_id>
        """
        pass

    def do_show(self, args):
        """
        Show string representation of an instance.
        Usage: Show <ClassName> <obj_id>
        """
        _class = self.parseline(args)[0]
        _id = self.parseline(args)[1]

        if _class is None:
            print('** class name missing **')
        elif _class not in self.classes:
            print("** class doesn't exist **")
        elif _id == '':
            print('** instance id missing **')
        else:
            inst_data = models.storage.all().get(_class + '.' + _id)
            if inst_data is None:
                print('** no instance found **')
            else:
                print(str(inst_data))

    def do_create(self, arg):
        """
        Create command to create a new instance of Airbnb models
        Usage: Create <ClassName>
        """
        token = self.parseline(arg)[0]

        if token is None:
            print('** class name missing **')
        elif token not in self.classes:
            print("** class doesn't exist **")
        else:
            new_obj = eval(token)()
            new_obj.save()
            print(new_obj.id)

    def do_quit(self, args):
        """
        Quit command exits out of the command interpreter
        """
        quit()

    def do_EOF(self, args):
        """
        EOF command exits out of the command interpreter
        """
        quit()

    def do_help(self, args):
        """
        Command lists all help details for each command
        """
        cmd.Cmd.do_help(self, args)

    def emptyline(self):
        """
        Returns back to the prompt
        """
        return

if __name__ == '__main__':
    HBNBCommand().cmdloop()
