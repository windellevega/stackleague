from fractions import *
import math
def decompose(n):
    # Egyptian Fraction using Fibonacci's algorithm
    if n == '0':
        return []

    decomposed = []

    n = n.split('/')

    if(len(n) == 2):
        numerator = is_numeric(n[0])
        denominator = is_numeric(n[1])

        if numerator > denominator:
            wholeNum = int(numerator/denominator)

            decomposed.append(str(wholeNum))
            numerator -= denominator * wholeNum

            if numerator % denominator == 0:
                return decomposed

        fraction = Fraction(numerator, denominator)
    else:
        fraction = Fraction(n[0])


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
        return int(n)
    else:
        raise ValueError

print(decompose('3/4'))
print(decompose('13/5'))
print(decompose('0.19'))
print(decompose('0.66'))
print(decompose('2/5'))
#print((1/2) + (1/7) + (1/59) + (1/5163) + (1/53307975))