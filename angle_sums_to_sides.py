import math
import itertools
import re
import operator
import collections


class AngleSumsToSides:

    def get_sum_of_interior_angles(self, sides):
        return 180 + (sides - 3) * 180

    def get_number_of_sides(self, sum_of_interior_angles):
        return ((sum_of_interior_angles) / 180) + 2

import unittest

class MyTestCase(unittest.TestCase):
    def test___SE___get_sum_of_interior_angles1(self):
        a = AngleSumsToSides()
        self.assertEqual(a.get_sum_of_interior_angles(3), 180)

    def test___SE___get_sum_of_interior_angles2(self):
        a = AngleSumsToSides()
        self.assertEqual(a.get_sum_of_interior_angles(7), 900)

    def test___SE___get_sum_of_interior_angles3(self):
        a = AngleSumsToSides()
        self.assertEqual(a.get_sum_of_interior_angles(13), 1980)

    def test___SE___get_sum_of_interior_angles4(self):
        a = AngleSumsToSides()
        self.assertEqual(a.get_sum_of_interior_angles(10), 1440)

    def test___SE___get_number_of_sides1(self):
        a = AngleSumsToSides()
        self.assertEqual(a.get_number_of_sides(180), 3)

    def test___SE___get_number_of_sides2(self):
        a = AngleSumsToSides()
        self.assertEqual(a.get_number_of_sides(900), 7)

    def test___SE___get_number_of_sides3(self):
        a = AngleSumsToSides()
        self.assertEqual(a.get_number_of_sides(1980), 13)

if __name__ == '__main__':
    unittest.main()