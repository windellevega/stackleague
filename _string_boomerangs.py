# In a string, there are these what we call "Boomerangs". We could easily determine them as substrings of three characters such that the first and last character are the same but not the middle character.
# For example: In a string `"PERSEVERANCEISTHEKEY"` we can identify `"EVE"` and `"EKE"` as string boomerangs.
# Write a function that will return the number of string boomerangs within an input string.

# NOTE:

# - There could be overlapping boomerangs on a string. (e.g. `"HAHA" -> "HAH", "AHA"`).
# - We don't consider a series of there character all with the same letters as boomerang (e.g. `"BOOOM" -> "OOO"` is not a boomerang).
# - You could assume that all inputs won't have white spaces and case insensitive.
# - String inputs should only include letters and numbers.
# - String inputs with less than 3 characters should return `NULL` or `None` (for Python)

import math
import itertools
import re
import operator
import collections

def count_string_boomerangs(string):
    count = 0
    if len(string) <= 2:
        return None

    string = string.lower()

    for i in range(len(string) - 2):
        if string[i] == string[i + 2] and string[i] != string[i + 1]:
            count += 1

    return count

######################### END OF SOLUTION #########################





import unittest

class MyTestCase(unittest.TestCase):
    # SAMPLE CASES
    def test___SE_SL_CS___sample1(self):
        self.assertEqual(count_string_boomerangs("PERSEVERANCEISTHEKEY"), 2)

    def test___SE_SL_CS___sample2(self):
        self.assertEqual(count_string_boomerangs("HAHA"), 2)

    def test___SE_SL_CS___sample3(self):
        self.assertIsNone(count_string_boomerangs("OH"))

    def test___SE_SL_CS___sample4(self):
        self.assertEqual(count_string_boomerangs("KSALALTXRXRV"), 4)

    def test___SE_SL_CS___sample5(self):
        self.assertEqual(count_string_boomerangs("boomerangs"), 0)

    # TEST CASES
    def test___SE_SL_CS___testcase1(self):
        self.assertEqual(count_string_boomerangs("pneumonoultramicroscopicsilicovolcanoconiosis"), 5)

    def test___SE_SL_CS___testcase2(self):
        self.assertIsNone(count_string_boomerangs(""))

    def test___SE_SL_CS___testcase3(self):
        self.assertEqual(count_string_boomerangs("aBA"), 1)

    def test___SE_SL_CS___testcase4(self):
        self.assertEqual(count_string_boomerangs("ASABXb2a823010aha"), 4)

    def test___SE_SL_CS___testcase5(self):
        self.assertEqual(count_string_boomerangs("aasddffgg"), 0)

if __name__ == '__main__':
    unittest.main()