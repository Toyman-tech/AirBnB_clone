#!/usr/bin/env python3
""" Defines the console or command line for AirBnB project """

import cmd


class HBNBCommand(cmd.Cmd):
    """ The base class for the console """

    prompt = "(hbnb) "

    def do_qiut(self, arg):
        """ Command to exit the console """

        return True

    def do_EOF(self, arg):
        """ Exit the console when calls EOF """

        return True

    def emptyline(self):
        """ Handle when empty line is entered """

        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
