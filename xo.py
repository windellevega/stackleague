def xo(names, number):
    namesSafe = []
    for name in names:
        if len(''.join(name.split(' '))) <= number:
            namesSafe.append(name)

    return namesSafe

print(xo(['Kyle', 'Christian', 'Ezekiel'], 5))
print(xo(['Kyle', 'Christian', 'Ezekiel'], -1))
print(xo(['Kyle', 'Christian', 'Ezekiel'], 0))
print(xo(['Kirsten', 'Johnny'], 8))