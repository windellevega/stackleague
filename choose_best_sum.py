import itertools
def choose_best_sum(t,k,ls):
    combos = list(itertools.combinations(ls,k))
    sums = [sum(i) for i in combos]
    sums2 = [i for i in sums if i<=t]
    if sums2 == []:
        largest = None
    else:
        largest = max([i for i in sums if i<=t])
    return largest