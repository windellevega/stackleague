def persistence(n):
    #code here
    ctr = 0

    while n >= 10:
        prod = 1
        for d in str(n):
            prod *= int(d)
        n = prod
        ctr += 1

    return ctr

print(persistence(30))
print(persistence(26))
print(persistence(254))

#2x5 = 10