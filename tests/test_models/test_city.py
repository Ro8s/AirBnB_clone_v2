#!/usr/bin/python3
''' Unittest for City '''

import models
import unittest
from models.base_model import BaseModel
from datetime import datetime
from models.city import City
import pep8


class TestCity(unittest.TestCase):
    ''' Test for City '''

    def test_city(self):
        '''  Test for City '''
        c = City(state_id="a", name="b")
        self.assertEqual(str, type(c.state_id))
        self.assertEqual(str, type(c.name))

    def test_pep8_console(self):
        """test pep8 style"""
        s = pep8.StyleGuide(quiet=True)
        pep = s.check_files(['models/city.py'])
        self.assertEqual(pep.total_errors, 0, 'Found errors.')

if __name__ == '__main__':
    unittest.main()
