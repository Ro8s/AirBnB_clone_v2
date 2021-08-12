#!/usr/bin/python3
"""Unittest for review"""
import models
import unittest
from models.base_model import BaseModel
from datetime import datetime
from models.review import Review
import pep8


class test_review(unittest.TestCase):
    """Test review"""

    def test_pep8_console(self):
        '''test pep8 style'''
        s = pep8.StyleGuide(quiet=True)
        pep = s.check_files(['models/review.py'])
        self.assertEqual(pep.total_errors, 0, 'Found errors.')

    def test_datatype(self):
        '''data type of review attributes'''
        r = Review(text="Volveatupaisquenosacaseltrabajoanosotors",
                   place_id="Rrrrum", user_id="Fium")
        self.assertEqual(str, type(r.text))
        self.assertEqual(str, type(r.place_id))
        self.assertEqual(str, type(r.user_id))
        self.assertEqual(r.__tablename__, 'reviews')

if __name__ == '__main__':
    unittest.main()
