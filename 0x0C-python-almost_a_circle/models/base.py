#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 15:43:09 2020

@author: meco
"""
import json


class Base:
    """
    Class Base

    Attributes:
        nb_objects (int): Private class attribute
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Class constructor

        Attributes:
            id (int): An integer input for id
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns a json string representation

        Attributes:
            list_dictionaries (json): An inputted jason list of dictionaries
        Return:
            A json repreentation
        """
        if list_dictionaries is None or not list_dictionaries:
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the json string repressentation list object to a file

        Attribute:
            list_objs (list): object list to save

        Return:
            json object to save in file
        """
        file_name = cls.__name__ + ".json"
        string = []
        if list_objs is not None:
            for i in list_objs:
                string.append(cls.to_dictionary(i))
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(cls.to_json_string(string))

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of json string representation

        Attribute:
            json_string (string): json object

        Return:
            json object to dictionary
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set

        Attribute:
            dictionary (dict): inooutted dictionary

        Return:
            An instance with all attributer already set
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances

        Return:
            A list of instances
        """
        file_name = cls.__name__ + ".json"
        json_obj = []
        try:
            with open(file_name, 'r', encoding='utf-8') as file:
                json_obj = cls.from_json_string(file.read())
            for key, value in enumerate(json_obj):
                json_obj[key] = cls.create(**json_obj[key])
        except:
            pass
        return json_obj
