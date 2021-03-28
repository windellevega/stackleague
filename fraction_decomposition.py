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
    print(n)
    numerator = n.numerator
    denominator = n.denominator

    if denominator == 0:
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
            fraction -= Fraction(1,startDen)
            decomposed.append('1/' + str(startDen))


    return decomposed
def is_numeric(n):
    if n.isnumeric():
        return True
    else:
        raise False

#print(str(Fraction('a')))
print(decompose('3/4'))
print(decompose('0.00056'))
print(decompose('0.19'))
print(decompose('0.66'))
print(decompose('0.43'))
#print((1/2) + (1/7) + (1/59) + (1/5163) + (1/53307975))