def words_reversed(string):
    string = string.split()
    for x in range(1, len(string), 2):
        string[x] = string[x][::-1]

    return ' '.join(string)

import unittest

class MyTestCase(unittest.TestCase):
    def test_example(self):
        self.assertEqual(words_reversed("I am omega!"), "I ma omega!");

    def test_double_spaced(self):
        self.assertEqual(words_reversed("Double  spaces"), "Double secaps");
if __name__ == '__main__':
    unittest.main()