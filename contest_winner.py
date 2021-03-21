def rank(st, we, n):
    if len(st) == 0:
        return 'No participants'

    alphabet = {
        'a' : 1,
        'b' : 2,
        'c' : 3,
        'd' : 4,
        'e' : 5,
        'f' : 6,
        'g' : 7,
        'h' : 8,
        'i' : 9,
        'j' : 10,
        'k' : 11,
        'l' : 12,
        'm' : 13,
        'n' : 14,
        'o' : 15,
        'p' : 16,
        'q' : 17,
        'r' : 18,
        's' : 19,
        't' : 20,
        'u' : 21,
        'v' : 22,
        'w' : 23,
        'x' : 24,
        'y' : 25,
        'z' : 26
    }
    nameRanks = {}
    st = st.split(',')
    if n > len(st):
        return 'Not enough participants'

    for name in enumerate(st):
        nameWeight = len(name[1])
        for letter in name[1]:
            nameWeight += alphabet[letter.lower()]

        nameRanks.update({ name[1] : nameWeight * we[name[0]] })

    nameRanks = dict(sorted(nameRanks.items(), key=lambda item: item[0]))
    nameRanks = dict(sorted(nameRanks.items(), key=lambda item: item[1], reverse=True))
    print(nameRanks)
    return list(nameRanks)[n - 1]
print(rank("Addison,Jayden,Sofia,Michael,Andrew,Lily,Benjamin", [4, 2, 1, 4, 3, 1, 2], 8))
print(rank("COLIN,AMANDBA,AMANDAB,CAROL,PauL,JOSEPH", [1, 4, 4, 5, 2, 1], 4))
print(rank("Elijah,Chloe,Elizabeth,Matthew,Natalie,Jayden", [1, 3, 5, 5, 3, 6], 2))
print(rank("Aubrey,Olivai,Abigail,Chloe,Andrew,Elizabeth", [3, 1, 4, 4, 3, 2], 4))