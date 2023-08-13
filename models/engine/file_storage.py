<<<<<<< HEAD
"""This module defines a class FileStorage that serializes instances to a JSON file and deserializes JSON file to instances"""
# import os
=======
"""This module defines a class FileStorage that serializes instances to a JSON
    file and deserializes JSON file to instances
"""
>>>>>>> 62e6906cbc16fb95e4289cbfd63df9ceabee2596
import json
# from models.base_model import BaseModel


class FileStorage:
    """serializes instances to a JSON file
    and deserializes JSON file to instances
    """

    # private instance attributes
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        # key = obj.__class__.__name__ + "." + obj.id
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file (path: __file_path)"""
        json_data = {}
<<<<<<< HEAD
        for key, value in self.__objects.items():
            json_data[key] = value.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(json_data, file)
            
    def reload(self):
        """ Reloads data
            Deserializes the JSON file to __objects
            But only if the JSON file (__file_path) exists;
            otherwise, it does nothing.
=======
        for key, obj in self.__objects.items():
            json_data[key] = obj.to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(json_data, file)

    def relaod(self):
        """Reloads data
        Deserializes the JSON file to __objects
        But only if the JSON file (__file_path) exists;
        otherwise, it does nothing.
>>>>>>> 62e6906cbc16fb95e4289cbfd63df9ceabee2596
        """
        from models.base_model import BaseModel
        self.__objects = {}  # Clear the __objects dictionary
        try:
<<<<<<< HEAD
            with open(self.__file_path, 'r') as file:
                # for key, value in json.load(file).items():
                #     self.new(dct[value[key]](**value))
=======
            with open(self.__file_path, "r") as file:
>>>>>>> 62e6906cbc16fb95e4289cbfd63df9ceabee2596
                data = json.load(file)
                for key, value in data.items():
                    # Create an instance of the class based on class_name
                    # set its attributes using the values from the dictionary
                    # then add it to __objects dictionary
<<<<<<< HEAD
                    # if key not in self.__objects:
                    nw_obj = eval(value['__class__'])(**value)
=======
                    nw_obj = eval(value["__class__"])(**value)
>>>>>>> 62e6906cbc16fb95e4289cbfd63df9ceabee2596
                    self.__objects[key] = nw_obj
                        # self.new(nw_obj)
        except FileNotFoundError:
            pass
<<<<<<< HEAD
        
=======
>>>>>>> 62e6906cbc16fb95e4289cbfd63df9ceabee2596
