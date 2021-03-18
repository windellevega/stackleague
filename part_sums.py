def part_sums(ls):
    sumsList = []
    lsLen = len(ls)
    tempSum = 0

    for ctr in range(lsLen):
        for num in range(ctr, lsLen):
            tempSum += ls[num]

        sumsList.append(tempSum)
        tempSum = 0

    sumsList.append(0)
    return sumsList


print(part_sums([]))