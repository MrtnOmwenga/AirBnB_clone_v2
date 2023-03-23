#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import models
import json
from models.state import State
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.user import User


classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is not None:
            obj_dict = {}
            for key, value in self.__objects.items():
                if cls == value.__class__ or cls == value.__class__.__name__:
                    obj_dict[key] = value
            return (obj_dict)
        return self.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        key = obj.to_dict()['__clas__']
        FileStorage.__objects.update({key + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }"""
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    x = FileStorage.__objects
                    x.[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """ Deletes object from __objects """
        if obj is not None:
            key = obj.__class__.__name__ + '.' + obj.id
            if key in self.__objects:
                del self.__objects[key]
