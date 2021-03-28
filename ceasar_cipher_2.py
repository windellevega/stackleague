import math
def moving_shift(string, shift):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encoded = ''
    for letter in enumerate(string):
        if letter[1].isupper():
            index = alphabet.index(letter[1].lower())
            encoded += alphabet[(index + shift) % 26].upper()
        elif letter[1].islower():
            index = alphabet.index(letter[1])
            encoded += alphabet[(index + shift) % 26]
        else:
            encoded += letter[1]
        shift += 1
    strlen = math.ceil(len(string) / 5)
    encoded = [encoded[i:i+strlen] for i in range(0, len(encoded), strlen)]
    if len(encoded) == 4:
        encoded.append('')
    return encoded
def demoving_shift(arr, shift):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    decoded = ''
    string = ''.join(arr)
    for letter in enumerate(string):
        if letter[1].isupper():
            index = alphabet.index(letter[1].lower())
            decoded += alphabet[(index - shift) % 26].upper()
        elif letter[1].islower():
            index = alphabet.index(letter[1])
            decoded += alphabet[(index - shift) % 26]
        else:
            decoded += letter[1]
        shift +=1
    return decoded

print(moving_shift("abcdefghjuty", 1))
print(moving_shift("abcdefghjuty1234", 1))
print(demoving_shift(["J vltasl rlhr ", "zdfog odxr ypw", " atasl rlhr p ", "gwkzzyq zntyhv", " lvz wp!!!"], 1))
u = "O CAPTAIN! my Captain! our fearful trip is done;"
print(demoving_shift(moving_shift(u, 1), 1))