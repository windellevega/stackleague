def parse(data):
    tempHopCtr = 0
    outputHops = []
    for char in data:
        if char.lower() == 'i':
            tempHopCtr += 1
        elif char.lower() == 'd':
            tempHopCtr -= 1
        elif char.lower() == 's':
            tempHopCtr *= tempHopCtr
        elif char.lower() == 'o':
            outputHops.append(tempHopCtr)

    return outputHops

print(parse('iiisdoso'))
print(parse('ixxiisadofso'))