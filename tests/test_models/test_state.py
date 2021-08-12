#!/usr/bin/python3
'''Unittest state'''
import models
import unittest
from models.base_model import BaseModel
from datetime import datetime
from models.state import State
import pep8


class TestState(unittest.TestCase):
    ''' Test for State'''
    def test_pep8_console(self):
        '''test pep8 style'''
        s = pep8.StyleGuide(quiet=True)
        pep = s.check_files(['models/state.py'])
        self.assertEqual(pep.total_errors, 0, 'Found errors.')

    def test_user(self):
        '''Test for State'''
        s = State(name='GuidoWazka')
        self.assertEqual(str, type(s.name))
        self.assertEqual(s.__tablename__, 'states')

if __name__ == '__main__':
    unittest.main()
