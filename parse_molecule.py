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

def parse_molecule_01(formula):
    """
    intuitive, left-to-right
    """
    tokens = [None, None]
    for token in formula:
        if token.isupper():
            tokens.append(token)
        elif token.islower():
            tokens[-1] += token
        elif token.isdigit():
            if tokens[-1].isdigit():
                tokens[-1] += token
            else:
                tokens.append(token)
        elif token in '{[(':
            tokens.append(token)
        elif token in ')]}':
            tokens.append(token)

    len_tokens = len(tokens)

    stack = [{}]

    def stack_push():
        stack.append({})

    def stack_pop():
        _hashtab_ = stack.pop()
        hashtab = stack[-1]
        for token in _hashtab_:
            hashtab[token] = hashtab.get(token, 0) + _hashtab_[token]

    def stack_pop_if(i):
        if tokens[i - 1] and tokens[i - 1].isdigit():
            hashtab = stack[-1]
            if tokens[i - 2] and tokens[i - 2].isalpha():
                hashtab[tokens[i - 2]] += int(tokens[i - 1]) - 1
            else:
                for _token_ in hashtab:
                    hashtab[_token_] *= int(tokens[i - 1])
                stack_pop()

    for i in range(2, len_tokens):
        token = tokens[i]
        if token.isalpha():
            stack_pop_if(i)
            hashtab = stack[-1]
            hashtab[token] = hashtab.get(token, 0) + 1
        elif token in '{[(':
            stack_pop_if(i)
            stack_push()
        elif token in ')]}':
            stack_pop_if(i)

    stack_pop_if(len_tokens)
    while len(stack) > 1:
        stack_pop()

    return stack[0]


print(parse_molecule('(H(O2))4'))
print(parse_molecule('Mg[((OH2]2'))
print(parse_molecule('AB4Au{[((OM2)2)4]2}2'))