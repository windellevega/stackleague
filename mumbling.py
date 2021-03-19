def mumbling(sequence):
    if not sequence.isalpha():
        return ""
    ctr = 0
    mumbled = ""
    for char in enumerate(sequence):
        mumbled += char[1].upper()
        for idx in range(ctr):
            mumbled += char[1].lower()
        if char[0] < len(sequence) -1:
            mumbled += "-"
        ctr += 1

    return mumbled

print(mumbling("RtXzY$"))