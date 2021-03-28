def dbl_linear(n):
    u = [1]
    x = 0
    y = 0

    while len(u) <= n:
        a = 2 * u[x] + 1
        b = 3 * u[y] + 1

        if a <= b:
            x += 1
        if a >= b:
            y += 1

        u.append(min(a,b))
    return u[n]
print(dbl_linear(100000))