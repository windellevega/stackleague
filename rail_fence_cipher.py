from itertools import cycle


def rail_pattern(n):
    r = list(range(n))
    return cycle(r + r[-2:0:-1])


def encode_rail_fence_cipher(s, n):
    p = rail_pattern(n)

    return ''.join(sorted(s, key=lambda i: next(p)))


def decode_rail_fence_cipher(s, n):
    p = rail_pattern(n)
    indexes = sorted(range(len(s)), key=lambda i: next(p))
    result = [''] * len(s)
    for i, c in zip(indexes, s):
        result[i] = c
    return ''.join(result)

print(encode_rail_fence_cipher('abcdefghijk', 3))
print(encode_rail_fence_cipher('Hello, World!', 2))