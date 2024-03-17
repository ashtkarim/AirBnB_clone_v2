#!/usr/bin/python3
"""
Module:console.py
"""

import cmd
import re
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    Create commande cmd
    """
    prompt = '(hbnb) '

    classes = {
        'BaseModel': BaseModel,
        'User': User,
        'Place': Place,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Review': Review
    }
    valid_keys = {
        "BaseModel": ["id", "created_at", "updated_at"],
        "User": [
            "id",
            "created_at",
            "updated_at",
            "email",
            "password",
            "first_name",
            "last_name",
        ],
        "City": ["id", "created_at", "updated_at", "state_id", "name"],
        "State": ["id", "created_at", "updated_at", "name"],
        "Place": [
            "id",
            "created_at",
            "updated_at",
            "city_id",
            "user_id",
            "name",
            "description",
            "number_rooms",
            "number_bathrooms",
            "max_guest",
            "price_by_night",
            "latitude",
            "longitude",
            "amenity_ids"
        ],
        "Amenity": ["id", "created_at", "updated_at", "name"],
        "Review": ["id", "created_at", "updated_at",
                   "place_id", "user_id", "text"],
    }

    def parse_value(self, value):
        """cast string to float or int if possible"""
        is_valid_value = True
        if len(value) >= 2 and value[0] == '"'\
                and value[len(value) - 1] == '"':
            value = value[1:-1]
            value = value.replace("_", " ")
        else:
            try:
                if "." in value:
                    value = float(value)
                else:
                    value = int(value)
            except ValueError:
                is_valid_value = False

        if is_valid_value:
            return value
        else:
            return None

    def do_quit(self, arg):
        """
        quit commande to EXIT the program
        """
        return True

    def do_EOF(self, line):
        """
        Ctrl+d commande to Exit the program
        """
        print("")
        return True

    def emptyline(self):
        """
        an empty line + ENTER shoudn't execute anything
        """
        pass

    def do_help(self, arg):
        """
        help function
        """
        return super().do_help(arg)

    def do_create(self, arg):
        """
        Create new instance
        """
        args_array = arg.split()
        class_name = args_array[0]
        if len(args_array) == 0:
            print("** class name missing **")
            return
        if args_array[0] not in self.classes.keys():
            print("** class doesn't exist **")
            return
        new_instance = HBNBCommand.classes[class_name]()
        for index in range(1, len(args_array)):
            param_array = args_array[index].split("=")
            if len(param_array) == 2:
                key = param_array[0]
                if key not in HBNBCommand.valid_keys[class_name]:
                    continue
                value = self.parse_value(param_array[1])
                if value is not None:
                    setattr(new_instance, key, value)
            else:
                pass
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """
        Show an instance with ID
        """
        args = arg.split()
        objects = storage.all()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.classes.keys():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        instances = objects.get(key, None)
        if instances is None:
            print("** no instance found **")
            return
        print(instances)

    def do_destroy(self, arg):
        """
        destroy an instance with ID
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.classes.keys():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        objects = storage.all()
        key = "{}.{}".format(args[0], args[1])
        if key in objects:
            del objects[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        """
        args = arg.split()
        objects = storage.all()

        if not args:
            print(["{}".format(v) for _, v in objects.items()])
            return
        if args[0] not in self.classes.keys():
            print("** class doesn't exist **")
            return
        else:
            class_name = args[0]
            class_objs = []
            for key, value in objects.items():
                if key.startswith(class_name + "."):
                    class_objs.append(str(value))
            print(class_objs)

    def do_update(self, arg):
        """
        Updates an instance
        """
        args = arg.split()
        objects = storage.all()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.classes.keys():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        instances = objects.get(key, None)
        if instances is None:
            print("** no instance found **")
            return
        """if not isinstance(args[3], (str, int, float)):
            print("** only simple arguments can be updated **")
            return"""
        setattr(instances, args[2], args[3].lstrip('"').rstrip('"'))
        storage.save()

    def do_count(self, arg):
        """ count  the number of instances of a given class."""
        argl = arg.split()
        count = 0
        for obj in storage.all().values():
            if argl[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def default(self, arg):
        """Default behavior for cmd module when input is invalid"""
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return argdict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
