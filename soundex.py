import re

def soundex(word):

    word = word.lower()
    if not re.match("^[a-z]+$", word):
        return False

    firstletter = word[0]
    result = []
    result.append(firstletter);

    word = re.sub(r'[aeiouyhw]*', '', word[1:])
    for letter in word:
        result.append(str(get_code(letter)));

    word = ''.join(result).upper();

    word = re.sub(r'([1-6])\1+', r'\1', word)

    if len(word) < 4:
        word += '0' * (4 - len(word))

    return word[:4]

def get_code(letter):
    codes = {'b': '1', 'f': '1', 'p': '1', 'v': '1', 'c': '2', 'g': '2', 'j': '2', 'k': '2', 'q': '2', 's': '2', 'x': '2', 'z': '2', 'd': '3', 't': '3', 'l': '4', 'm': '5', 'n': '5', 'r': '6'}
    return int(codes[letter.lower()]);

print(soundex('Robert'))
print(soundex('Rupert'))
print(soundex('Rubin'))
print(soundex('Ashcraft'))
print(soundex('Ashcroft'))
print(soundex('Ashcra@@@ft'))
print(soundex('WindelleJohn'))