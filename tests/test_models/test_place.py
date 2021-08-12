#!/usr/bin/python3
''' Unittest for Place '''

import models
import unittest
from models.base_model import BaseModel
from datetime import datetime
from models.place import Place
import pep8


class TestUser(unittest.TestCase):
    ''' Test for Place'''

    def test_user(self):
        '''  Test for User '''
        p = Place(city_id="a", user_id="b", name="eman", number_rooms=0,
                  number_bathrooms=69, max_guest=777, price_by_night=15,
                  latitude=0.0, longitude=0.1, amenity_ids=[])
        self.assertEqual(str, type(p.city_id))
        self.assertEqual(str, type(p.user_id))
        self.assertEqual(str, type(p.name))
        self.assertEqual(int, type(p.number_rooms))
        self.assertEqual(int, type(p.number_bathrooms))
        self.assertEqual(int, type(p.max_guest))
        self.assertEqual(int, type(p.price_by_night))
        self.assertEqual(float, type(p.latitude))
        self.assertEqual(float, type(p.longitude))
        self.assertEqual(list, type(p.amenity_ids))

    def test_pep8_console(self):
        """test pep8 style"""
        s = pep8.StyleGuide(quiet=True)
        pep = s.check_files(['models/place.py'])
        self.assertEqual(pep.total_errors, 0, 'Found errors.')

if __name__ == '__main__':
    unittest.main()
