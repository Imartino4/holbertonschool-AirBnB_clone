#!/usr/bin/python3
""" Console Module """

import cmd, shlex
from models.base_model import BaseModel
from models import storage

classes = {'BaseModel': BaseModel, 'User': User, 'State': State,
        'City': City, 'Amenity': Amenity, 'Place': Place, 'Review': Review}

def class_check(input_str):
    input = input_str.split()
    if len(input_str) == 0:
        print("** class name missing **")
        return False
    if input[0] not in classes.keys():
        print("** class doesn't exist **")
        return False
    return True

def id_check(input_str):
    input = input_str.split()
    try:
        id = input[1]
        all_objs = storage.all()
        if f"{input[0]}.{id}" in all_objs.keys():
            return True
        else:
            print("** no instance found **")
            return False
    except Exception:
        print("** instance id missing **")


class HBNBCommand(cmd.Cmd):
    """ Class Holberton CMD """
    prompt = "(hbnb)"

    def do_quit(self, arg):
        """ Quit command to exit program """
        return True

    def do_EOF(self, arg):
        """ Exits program on EOF. """
        return True

    def emptyline(self):
        pass

    def do_create(self, arg):
        if class_check(arg):
            new_obj = classes[arg]()
            new_obj.save()
            print(new_obj.id)

    def do_show(self, arg):
        args = arg.split()
        if class_check(arg) and id_check(arg):
            objs = storage.all()
            print(objs[f"{args[0]}.{args[1]}"])

    def do_destroy(self, arg):
        args = arg.split()
        if class_check(arg) and id_check(arg):
            del storage.all()[f"{args[0]}.{args[1]}"]
            storage.save()

    def do_all(self, arg):
        args = arg.split()
        objects = storage.all()
        list_obj = []

        if len(arg) == 0:
            for obj in objects.values():
                list_obj.append(obj.__str__())
            print (list_obj)
        if len(args) == 1:
            if class_check(arg):
                for obj in objects.values():
                    if obj.__class__.__name__ == args[0]:
                        list_obj.append(obj.__str__())
                print(list_obj)
                    
    def do_update(self, arg):
        args = shlex.split(arg)
        if class_check(arg) and id_check(arg):
            if len(args) == 2:
                print("** attribute name missing **")
            elif len(args) == 3:
                print("** value missing **")
            else:
                obj = storage.all()[f"{args[0]}.{args[1]}"]
                setattr(obj, args[2], args[3])
                storage.save()
                
if __name__ == '__main__':
    HBNBCommand().cmdloop()
