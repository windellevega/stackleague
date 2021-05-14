import math
def diophantus(n):
    result = []

    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i != 0:
            continue

        j = n / i
        y = (j - i) / 4
        x = i + 2 * y

        if x >= 0 and y >= 0 and (j == x + 2 * y) and (i == x - 2 * y) and x.is_integer() and y.is_integer():
            result.append([int(x), int(y)])

    return sorted(result, reverse=True)

print(diophantus(12))
print(diophantus(13))
print(diophantus(16))
print(diophantus(17))
print(diophantus(90005))
print(diophantus(90002))