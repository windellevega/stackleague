import math
def buddy(start, limit):
    sums = []

    for i in range(start, limit):
        sumn = get_sum_divisors(i)
        if sumn > i + 1:
            summ = get_sum_divisors(sumn - 1)
            if i == summ - 1:
                return [i, sumn - 1]

    return 'Nothing'

def get_sum_divisors(n):
    sum = 0
    for i in range(1, math.ceil(math.sqrt(n))):
        if n % i == 0:
            if n / i == i:
                sum += i
            else:
                sum += i + n / i
    return int(sum - n)

print(buddy(310, 2755))
print(buddy(1071625, 1103735))
print(buddy(57345, 90061))
print(buddy(10, 50))
print(buddy(48, 50))