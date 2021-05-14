import math


def number_to_roman(number):
    romanDict = {
        1: "I",
        5: "V",
        10: "X",
        50: "L",
        100: "C",
        500: "D",
        1000: "M",
        5000: "G",
        10000: "H"
    }

    div = 1

    while number >= div:
        div *= 10

    div /= 10

    res = ""

    while number:
        lastNum = int(number / div)

        if lastNum <= 3:
            res += (romanDict[div] * lastNum)
        elif lastNum == 4:
            res += (romanDict[div] + romanDict[div * 5])
        elif 5 <= lastNum <= 8:
            res += (romanDict[div * 5] + (romanDict[div] * (lastNum - 5)))
        elif lastNum == 9:
            res += (romanDict[div] + romanDict[div * 10])

        number = math.floor(number % div)
        div /= 10

    return res

import unittest

class MyTestCase(unittest.TestCase):
    def test___sample_1(self):
        self.assertEqual(number_to_roman(1), 'I')

    def test___sample_2(self):
        self.assertEqual(number_to_roman(4), 'IV')

    def test___sample_3(self):
        self.assertEqual(number_to_roman(5), 'V')

    def test___sample_4(self):
        self.assertEqual(number_to_roman(9), 'IX')

    def test___sample_5(self):
        self.assertEqual(number_to_roman(19), 'XIX')

    def test___sample_6(self):
        self.assertEqual(number_to_roman(22), 'XXII')

    def test___sample_7(self):
        self.assertEqual(number_to_roman(15), 'XV')


if __name__ == '__main__':
    unittest.main()