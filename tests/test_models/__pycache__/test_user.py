#!/usr/bin/python3
""" User unittests"""
import unittest
from models.user import User
import pep8


class test_User(unittest.TestCase):
    """Test for user"""
    def test_user(self):
        '''  Test for User '''
        u = User(email='Benny@mailcaliente.com', password='FichadePlatino',
                 first_name='Benito', last_name='Camelo')
        self.assertEqual(str, type(u.email))
        self.assertEqual(str, type(u.password))
        self.assertEqual(str, type(u.first_name))
        self.assertEqual(str, type(u.last_name))

    def test_pep8_console(self):
        """test pep8 style"""
        s = pep8.StyleGuide(quiet=True)
        pep = s.check_files(['models/user.py'])
        self.assertEqual(pep.total_errors, 0, 'Found errors.')

if __name__ == '__main__':
    unittest.main()
