def duplicate_encode(word):
    word = word.lower()
    encoded = ''

    for char in word:
        if word.count(char) > 1:
            encoded += ')'
        else:
            encoded += '('

    return encoded

print(duplicate_encode('abc'))
print(duplicate_encode('aaaa'))
print(duplicate_encode('recede'))