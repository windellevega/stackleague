import re

def mix(s1, s2):
    s1 = sorted(re.sub('[^a-z]+', '', s1))
    s2 = sorted(re.sub('[^a-z]+', '', s2))
    counts = {'1':{},'2':{}, '=':{}}
    diff = []
    ptr = 0
    temp = ''
    while ptr < len(s1):
        if(s1[ptr] != temp):
            counts['1'][s1[ptr]] = s1.count(s1[ptr])
            temp = s1[ptr]
        ptr += 1
    ptr = 0
    temp = ''

    while ptr < len(s2):
        if(s2[ptr] != temp):
            if not s2[ptr] in counts['1']:
                counts['2'][s2[ptr]] = s2.count(s2[ptr])
            elif counts['1'][s2[ptr]] < s2.count(s2[ptr]):
                counts['2'][s2[ptr]] = s2.count(s2[ptr])
                del counts['1'][s2[ptr]]
            elif counts['1'][s2[ptr]] == s2.count(s2[ptr]):
                counts['='][s2[ptr]] = s2.count(s2[ptr])
                del counts['1'][s2[ptr]]
            temp = s2[ptr]
        ptr += 1

    for val in counts['1']:
        if(counts['1'][val] > 1):
            diff.append('1:' + counts['1'][val] * val)

    for val in counts['2']:
        if (counts['2'][val] > 1):
            diff.append('2:' + counts['2'][val] * val)

    for val in counts['=']:
        if (counts['='][val] > 1):
            diff.append('=:' + counts['='][val] * val)

    diff = sorted(diff, key=len, reverse=True)
    return ('/'.join(diff))


print(mix('my&friend&Paul has heavy hats! &', 'my friend John has many many friends &'))