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
            numerator -= denominator

            if numerator % denominator == 0:
                return decomposed

        decimalVal = numerator/denominator
    else:
        decimalVal = float(n[0])


    startDen = 2
    sumDecompose = 0

    while round(decimalVal, 7) != round(sumDecompose, 7):
        temp = 1 / startDen
        if sumDecompose + temp <= decimalVal:
            sumDecompose += temp
            decomposed.append('1/' + str(startDen))
        startDen += 1


    return decomposed
def is_numeric(n):
    if n.isnumeric():
        return int(n)
    else:
        raise ValueError

print(decompose('0.66'))
print(decompose('3/4'))
print(decompose('13/5'))
#print((1/2) + (1/7) + (1/59) + (1/5163) + (1/53307975))