def countBits(n):
    binaryString = '{0:b}'.format(n)
    ctr = 0
    for bit in binaryString:
        if bit == '1':
            ctr += 1
    return ctr

print(countBits(7))