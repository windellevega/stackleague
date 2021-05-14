import math
def duration(v0, slope, d_tot):
    # d_tot = total kilometers
    # slope = slope %
    # v0 = speed at t = 0
    #initial acceleration gamme = 0 (km/h/min)

    MASS = 80.0 # mass
    WATTS0 = 225.0 # start pedaling power
    DELTA_T = 1.0/60.0 # time step
    G_THRUST = 60 * 3.6 * 3.6
    GRAVITY_ACC = 9.81 * 3.6 * 60.0
    DRAG = 60.0 * 0.3 / 3.6
    D_WATTS = 0.5

    gamma = 0.0
    watts = WATTS0
    d = 0.0
    v = v0 # current speed
    slope = math.sin(math.atan(slope / 100))
    t = 0.0
    air_drag = 0.0

    while d <= d_tot:
        #print(d)
        t += DELTA_T
        watts -= D_WATTS * DELTA_T

        gamma = -GRAVITY_ACC * slope
        air_drag = -DRAG * abs(v) * abs(v) / MASS
        gamma += air_drag

        if watts > 0.0 and v > 0.0:
            gamma += G_THRUST * watts / (v * MASS)

        if abs(gamma) <= 0.00001:
            gamma = 0.0

        v += gamma * DELTA_T
        d += v * DELTA_T / 60.0
        #print(gamma)



        if v - 3.0 <= 0.01:
            return -1
        #print(d, v, t)

    return round(t)

print(duration(30, 5, 30))
print(duration(30, 20, 30))
print(duration(30, 8, 20))
print(duration(30, 0, 5))
print(duration(50, 10, 25))