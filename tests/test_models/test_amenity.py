#!/usr/bin/python3
''' Unittest for Amenity '''

import models
import unittest
from models.base_model import BaseModel
from datetime import datetime
from models.amenity import Amenity
import pep8


class TestAmenity(unittest.TestCase):
    ''' Test for User'''

    def test_amenity(self):
        '''  Test for Amenity '''
        a = Amenity(name="a")
        self.assertEqual(str, type(a.name))

    def test_pep8_console(self):
        """test pep8 style"""
        s = pep8.StyleGuide(quiet=True)
        pep = s.check_files(['models/amenity.py'])
        self.assertEqual(pep.total_errors, 0, 'Found errors.')

if __name__ == '__main__':
    unittest.main()
