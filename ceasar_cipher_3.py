import math
def encode_str(string, shift):
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
        if letter[0] == 0:
            encoded = string[0].lower() + encoded.lower() + encoded
    strlen = math.ceil((len(string) + 2) / 5)
    encoded = [encoded[i:i+strlen] for i in range(0, len(encoded), strlen)]

    return encoded
def decode(arr):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    decoded = ''
    string = ''.join(arr)

    shift = alphabet.find(string[1]) - alphabet.find(string[0])
    string = string[2:len(string)]
    for letter in enumerate(string):
        if letter[1].isupper():
            index = alphabet.index(letter[1].lower())
            decoded += alphabet[(index - shift) % 26].upper()
        elif letter[1].islower():
            index = alphabet.index(letter[1])
            decoded += alphabet[(index - shift) % 26]
        else:
            decoded += letter[1]
    return decoded

u = "I should have known that you would have a perfect answer for me!!!"
v = ["ijJ tipvme ibw", "f lopxo uibu z", "pv xpvme ibwf ", "b qfsgfdu botx", "fs gps nf!!!"]
print(encode_str(u, 1))
print(decode(v))
u = "abcdefghjuty12"
v = ["abbc", "defg", "hikv", "uz12"]
print(encode_str(u, 1))
print(decode(v))