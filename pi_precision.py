import math
def iter_pi(epsilon):
    result = 0.0
    n = 0
    while True:
        result += (-1.0) ** n / (2.0 * n + 1.0)
        n += 1
        if abs(math.pi - (result * 4)) < epsilon:
            return [n, float('{0:.10f}'.format(4*result))]
print(iter_pi(0.01))