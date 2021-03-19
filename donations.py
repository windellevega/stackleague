import math
def new_avg(arr, newavg):
    sumarr = 0
    arrlen = len(arr) + 1
    nextdonate = 0
    for num in arr:
        sumarr += num

    nextdonate = (newavg * arrlen) - sumarr

    if nextdonate <= 0:
        raise ValueError

    return math.ceil(nextdonate)

print(new_avg ([14, 30, 5, 7, 9, 11, 16], 90))