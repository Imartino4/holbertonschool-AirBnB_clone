#!/usr/bin/python3
""" Console Module """

import cmd
import shlex
from models.base_model import BaseModel
from models import user, state, city, amenity, place, review
from models import storage

# Classes dictionary storing keys with classes
# names in strings and values with  the actual class.
classes = {
    'BaseModel': BaseModel,
    'User': user.User,
    'State': state.State,
    'City': city.City,
    'Amenity': amenity.Amenity,
    'Place': place.Place,
    'Review': review.Review
    }


def class_check(input_str):
    """
        Validates:
            - input_str is non empty
            - input_str refers to an existing class
    """
    input = input_str.split()
    if len(input_str) == 0:
        print("** class name missing **")
        return False
    if input[0] not in classes.keys():
        print("** class doesn't exist **")
        return False
    return True


def id_check(input_str):
    """
        Validates:
            - input_str contains an id
            - id exists in storage
    """
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
        """ Emptyline command  customized"""
        pass

    def do_create(self, arg):
        """ Create new instance
            Usage: create <class name>
        """
        if class_check(arg):
            new_obj = classes[arg]()
            new_obj.save()
            print(new_obj.id)

    def do_show(self, arg):
        """ Print the string representation of an instance
            Usage: show <class name> <id>
        """
        args = arg.split()
        if class_check(arg) and id_check(arg):
            objs = storage.all()
            print(objs[f"{args[0]}.{args[1]}"])

    def do_destroy(self, arg):
        """
            Delete an instance
            Usage: destroy <class name> <id>
        """
        args = arg.split()
        if class_check(arg) and id_check(arg):
            del storage.all()[f"{args[0]}.{args[1]}"]
            storage.save()

    def do_all(self, arg):
        """
            Print all instances with specific class or not
            Usage: -all <class name>
                   -all
        """
        args = arg.split()
        objects = storage.all()
        list_obj = []

        if len(arg) == 0:
            for obj in objects.values():
                list_obj.append(obj.__str__())
            print(list_obj)
        if len(args) == 1:
            if class_check(arg):
                for obj in objects.values():
                    if obj.__class__.__name__ == args[0]:
                        list_obj.append(obj.__str__())
                print(list_obj)

    def do_update(self, arg):
        """
            Update an instance's attribute or create new one.
            Usage: update <class name> <id> <attribute> <value_attribute>
        """
        args = shlex.split(arg)
        if class_check(arg) and id_check(arg):
            if len(args) == 2:
                print("** attribute name missing **")
            elif len(args) == 3:
                print("** value missing **")
            else:
                obj = storage.all()[f"{args[0]}.{args[1]}"]
                if args[3].isnumeric():
                    args[3] = int(args[3])
                setattr(obj, args[2], args[3])
                storage.save()

    def default(self, arg):
        """
            Custom default function for other miscellaneous commands
        """
        count = 0
        args = arg.split(".")
        if len(args) == 2 and class_check(args[0]):
            clase = args[0]
            method = args[1]

            if 'all()' == method:
                self.do_all(clase)
            elif 'count()' == method:
                for obj in storage.all().values():
                    if obj.__class__.__name__ == clase:
                        count += 1
                print(count)
            elif 'show' in method:
                obj_id = args[1][6:-2]
                self.do_show(f"{args[0]} {obj_id}")
            elif 'destroy' in method:
                obj_id = args[1][9:-2]
                self.do_destroy(f"{args[0]} {obj_id}")
            elif 'update' in method:
                list_aux = args[1].split(', ')
                obj_id = list_aux[0][8:-1]
                print(obj_id)
                attr = list_aux[1][1:-1]
                print(attr)
                attr_val = list_aux[2][:-1]
                print(attr_val)
                if attr_val[0] == '"':
                    attr_val = attr_val[1:-1]
                self.do_update(f"{clase} {obj_id} {attr} {attr_val}")
            else:
                print(f"*** Unknwon method {method} for class: {clase}")
        else:
            print(f"*** Unknown syntax: {arg}")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
