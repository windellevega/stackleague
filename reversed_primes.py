import math
def find_emirp(n):
    sumEmirps = 0
    totalEmirps = 0
    largestEmirps = 0

    for x in range(13, n + 1):
        rev = int(str(x)[::-1])

        if is_prime(x) and is_prime(rev) and x % 10 != 0 and x != rev:
            sumEmirps += x
            totalEmirps += 1
            largestEmirps = x
    return [totalEmirps, largestEmirps, sumEmirps]

def is_prime(n):
    for x in range(2, math.ceil(math.sqrt(n)) + 1):
        if n % x == 0:
            return False

    return True

print(find_emirp(50))
print(find_emirp(100))
print(find_emirp(200))