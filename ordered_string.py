def ordered_string(sentence):
    mapSentence = {}
    sentence = sentence.split()
    for i in sentence:
        mapSentence[int(''.join(filter(str.isdigit, i)))] = i

    return ' '.join([mapSentence[x] for x in sorted(mapSentence)])

print(ordered_string('strin3gs order1 please4 2the'))
print(ordered_string("insi2de o3f hea5rt m4y co1me"))