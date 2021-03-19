def nbMonths(old, new, saving, percent) :
    oldPriceDep = old
    newPriceDep = new
    available = -99999.00
    months = 1
    result = []

    if new <= old :
        result.append(0)
        result.append(old - new)
        return result

    while available < 0 :
        if months % 2 == 0 :
            percent += 0.5
        percentMult = 1.0 - (percent / 100)
        oldPriceDep = oldPriceDep * percentMult
        newPriceDep = newPriceDep * percentMult
        available = (oldPriceDep + saving * months) - newPriceDep
        months += 1

    result.append(months - 1)
    result.append(round(available))
    return result


print(nbMonths(2000, 8000, 1000, 1.5))
print(nbMonths(12000, 8000, 1000, 1.5))