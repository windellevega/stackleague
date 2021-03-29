def nb_year(population, percent, additional, target):
    #code here
    percent = percent / 100
    ctr = 0
    while population < target:
        population += int(population * percent)
        population += additional
        ctr += 1

    return ctr

print(nb_year(1500, 5, 100, 5000))
print(nb_year(1500000, 2.5, 10000, 2000000))