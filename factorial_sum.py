def factorial_sum(lst):
    prime_list = []
    final_list = []
    for n in lst:
        prime_list = list(set(prime_list).union(set(prime_factors(n))))
    prime_list.sort()
    for n in prime_list:
        sum = 0
        list_n = [n]
        for m in lst:
            if m % n == 0:
                sum = sum + m
        list_n.append(sum)
        final_list.append(list_n)
    return final_list


def prime_factors(n):
    i = 2
    n = abs(n)
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

print(factorial_sum([12, 15, -51]))
print(factorial_sum([-43,-21,-24,-33,-45,-13, -25, -234, -63, -24]))
print(factorial_sum([107, 158, 204, 100, 118, 123, 126, 110, 116, 100]))
print(factorial_sum([-29804, -4209, -28265, -72769, -31744]))
