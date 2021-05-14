import itertools
def next_bigger(number):
    digits = list(str(number))

    for i in range(len(digits) - 2, -1, -1):
        if digits[i] < digits[i + 1]:
            temp = digits[i:]
            m = min(filter(lambda x: x > temp[0], temp))
            temp.remove(m)
            temp.sort()
            digits[i:] = [m] + temp
            return int("".join(digits))

    return -1

print(next_bigger(790))
print(next_bigger(670))
# for x in range(99999):
#     print(next_bigger(x))