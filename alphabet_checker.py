def check(chars):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    startPos = alphabet.find(chars[0].lower())

    for char in chars:
        if char.lower() != alphabet[startPos]:
            if char.isupper():
                return alphabet[startPos].upper()
            else:
                return alphabet[startPos]
        startPos += 1

    raise ValueError("No missing letter")

print(check(['A', 'C', 'D']))
print(check(['a', 'c', 'd']))
print(check(['e', 'f', 'g']))
print(check(['h','i','k']))