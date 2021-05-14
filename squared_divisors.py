import math


def list_squared(m, n):
    nlist = []
    for i in range(m, n + 1):
        sumDivs = sum_square_divs(i)
        if int(math.sqrt(sumDivs) + 0.5) ** 2 == sumDivs:
            nlist.append([i, sumDivs])

    return nlist

def sum_square_divs(n):
    sum = 0
    for i in range(1, n + 1):
        if n % i == 0:
            sum += (i ** 2)

    return sum


import unittest

class MyTestCase(unittest.TestCase):
    def test___DS___case_1(self):
        self.assertEqual(list_squared(1, 250), [[1, 1], [42, 2500], [246, 84100]])

    def test___DS___case_2(self):
        self.assertEqual(list_squared(42, 250), [[42, 2500], [246, 84100]])

if __name__ == '__main__':
    unittest.main()