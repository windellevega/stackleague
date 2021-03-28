import re
from collections import Counter

def parse_molecule(formula):

    array = [[]]

    for token in re.findall('[A-Z][a-z]?|\d+|.', formula):
        if token.isalpha():
            last = [token]
            upper = token
            array[-1].append(token)
        elif token.isdecimal():
            count = int(token)
            array[-1].extend(last * (int(token) - 1))
        elif token in ['(', '[', '{']:
            array.append([])
        elif token in [')', ']', '}']:
            last = array.pop()
            array[-1].extend(last)

    return dict(Counter(array[-1]))


print(parse_molecule('(H(O2))4'))
print(parse_molecule('Mg[((OH2]2'))
print(parse_molecule('AB4Au{[((OM2)2)4]2}2'))