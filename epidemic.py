def epidemic(tm, n, s, i, b, a):
    dt = tm/n
    time = 0
    r = 0
    imax = 0

    for t in range(int(tm/dt)):
        bsi = b * s * i
        ai = a * i

        r += dt * ai
        i += dt * (bsi - ai)
        s -= dt * bsi

        if i > imax:
            imax = i

    return int(imax)

tm = 18; n = 432; s0 = 1004; i0 = 1; b = 0.00209; a = 0.51
print(epidemic(tm, n, s0, i0, b, a)) # 420

tm = 12; n = 288; s0 = 1007; i0 = 2; b = 0.00206; a = 0.45
print(epidemic(tm, n, s0, i0, b, a)) # 461

tm = 14; n = 336; s0 = 996; i0 = 2; b = 0.00206; a = 0.41
print(epidemic(tm, n, s0, i0, b, a)) # 483

tm = 14; n = 336; s0 = 999; i0 = 1; b = 0.00118; a = 0.5
print(epidemic(tm, n, s0, i0, b, a)) #214