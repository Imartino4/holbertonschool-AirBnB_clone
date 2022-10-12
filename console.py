#!/usr/bin/python3
""" Console Module """

import cmd

class HBNBCommand(cmd.Cmd):
    """ Class Holberton CMD """
    prompt = "(hbnb)"

    def do_quit(self, arg):
        """ Quit command to exit program """
        raise SystemExit

    def do_EOF(self, arg):
        """ Exits program on EOF """
        raise SystemExit

    def emptyline(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()