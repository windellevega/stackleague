def decomp(n):
    decomposedFact = []
    for factor in range(2, n + 1):
        if is_prime(factor):
            decomposedFact.append(factor)
        else:
            primeF = get_prime_factors((factor))
            decomposedFact += get_prime_factors(factor)
    decomposedFact = sorted(decomposedFact)

    result = []
    for pfactor in decomposedFact:
        pfcount = decomposedFact.count(pfactor)
        if pfcount == 1:
            result.append(str(pfactor))
        elif pfcount > 1:
            result.append(str(pfactor) + '^' + str(pfcount))
        decomposedFact = remove_values_from_list(decomposedFact, pfactor)
    return ' * '.join(result)

def remove_values_from_list(the_list, val):
   return [value for value in the_list if value != val]


def get_prime_factors(n):
    prime_factors = []

    x = 2

    while not is_prime(n):
        if n % x == 0:
            if is_prime(x):
                prime_factors.append(x)
                n = int(n / x)
                x = 2
        else:
            x += 1

    prime_factors.append(n)
    return prime_factors

def is_prime(n):
    if (n <= 1):
        return False
    if (n <= 3):
        return True

    if (n % 2 == 0 or n % 3 == 0):
        return False

    i = 5
    while (i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i = i + 6

    return True

print(decomp(5))
print(decomp(12))
print(decomp(22))
print(decomp(25))
print(get_prime_factors(100))
print(get_prime_factors(1000))
print(get_prime_factors(999))
print(get_prime_factors(53))