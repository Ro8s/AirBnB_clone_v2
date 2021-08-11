#!/usr/bin/python3
''' Unittest for console '''

import unittest
from unittest.mock import patch
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from console import HBNBCommand
from io import StringIO
import pep8


class Test_Console(unittest.TestCase):
    '''Unittest for ex 2'''
    
    def test_pep8_console(self):
        """test pep8 style"""
        s = pep8.StyleGuide(quiet=True)
        pep = s.check_files(['console.py'])
        self.assertEqual(pep.total_errors, 0, 'Found errors.')
    
    def test_create_no_class(self):
        """create test w/o class"""
        self.consola = HBNBCommand()
        with patch('sys.stdout', new=StringIO()) as out:
            self.consola.onecmd("create")
        self.assertEqual("** class name missing **\n", out.getvalue())

    def test_create_not_a_class(self):
        """create test w/ non existing class"""
        self.consola = HBNBCommand()
        with patch('sys.stdout', new=StringIO()) as out:
            self.consola.onecmd("create Danitkm")
        self.assertEqual("** class doesn't exist **\n", out.getvalue())
