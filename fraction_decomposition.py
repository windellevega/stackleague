from fractions import *
import math
def decompose(n):
    # Egyptian Fraction using Fibonacci's algorithm
    if n.split('/')[0] == '0':
        return []

    decomposed = []

    if Fraction(n).denominator == 1:
        return [str(Fraction(n).numerator)]

    n = Fraction(n)
    #print(n)
    numerator = n.numerator
    denominator = n.denominator

    if denominator == 0 or numerator < 0:
        raise ValueError

    if numerator > denominator:
        wholeNum = int(numerator/denominator)

        decomposed.append(str(wholeNum))
        numerator -= denominator * wholeNum

        if numerator % denominator == 0:
            return decomposed

    fraction = Fraction(numerator, denominator)

    startDen = 0

    while fraction.numerator != Fraction(0):
            # denominator of the largest fraction you can subtract from
            # a fraction is d = ceil(denominator / numerator)
            # e.g. 4/5 -> ceil(5/4) = ceil(1.25) = 2 -> 1/2
            startDen = math.ceil(fraction.denominator / fraction.numerator)
            #print(startDen)
            fraction -= Fraction(1,startDen)
            decomposed.append('1/' + str(startDen))

    return decomposed

def is_numeric(n):
    if not n.isnumeric():
        raise ValueError
    n = Fraction(n)
    # print(n)
    numerator = n.numerator
    denominator = n.denominator

    if denominator == 0 or numerator < 0:
        raise ValueError


import unittest

class MyTestCase(unittest.TestCase):
    def test___AL___sample_test_1(self):
        self.assertEqual(decompose('0'), [])

    def test___AL___sample_test_2(self):
        self.assertEqual(decompose('3/4'), ["1/2", "1/4"])

    def test___AL___sample_test_3(self):
        self.assertEqual(decompose('4/5'), ["1/2", "1/4", "1/20"])

    def test___AL___sample_test_4(self):
        self.assertEqual(decompose('0.66'), ["1/2", "1/7", "1/59", "1/5163", "1/53307975"])

    def test___AL___sample_test_5(self):
        self.assertEqual(decompose('75/3'), ["25"])

    def test___AL___sample_test_6(self):
        self.assertEqual(decompose('13/12'), ["1", "1/12"])

    def test___AL___sample_test_7(self):
        self.assertEqual(decompose('21/23'), ["1/2", "1/3", "1/13", "1/359", "1/644046"])

if __name__ == '__main__':
    unittest.main()
#print((1/2) + (1/7) + (1/59) + (1/5163) + (1/53307975))