from fractions import *
import math
def decompose(n):
    if n == '0':
        return []
    n = n.split('/')
    decomposed = []

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
    sumDecompose = Fraction(0)

    while fraction.numerator != Fraction(0):
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
#print((1/2) + (1/7) + (1/59) + (1/5163) + (1/53307975))