def next_smaller(number):
    digits = list(str(number))
    i = j = len(digits) - 1
    while i > 0 and digits[i - 1] <= digits[i]:
        i -= 1
    if i <= 0:
        return -1
    while digits[j] >= digits[i - 1]:
        j -= 1
    digits[i - 1], digits[j] = digits[j], digits[i - 1]
    digits[i:] = reversed(digits[i:])
    if digits[0] == '0':
        return -1
    return int(''.join(digits))


import unittest

class MyTestCase(unittest.TestCase):
    def test___one(self):
        self.assertEqual(next_smaller(21), 12)

    def test___two(self):
        self.assertEqual(next_smaller(907), 790)

    def test___three(self):
        self.assertEqual(next_smaller(1027), -1)

    def test___four(self):
        self.assertEqual(next_smaller(5402), 5240)


if __name__ == '__main__':
    unittest.main()