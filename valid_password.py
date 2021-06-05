import math
import itertools
import re
import operator
import collections

def validate(password):
    if len(password) < 8:
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if any(char == ' ' or char == '_' for char in password):
        return False
    if not any(char in ('!@#$%^&*()') for char in password):
        return False

    return True

######################### END OF SOLUTION #########################





import unittest

class MyTestCase(unittest.TestCase):
    def test___password(self):
        self.assertEqual(validate("Asfdasdf!234"), True)

    def test___white_spaces(self):
        self.assertEqual(validate("Asfdasdf !234"), False)

    def test___no_upper_case(self):
        self.assertEqual(validate("sfdasdf!234"), False)

if __name__ == '__main__':
    unittest.main()