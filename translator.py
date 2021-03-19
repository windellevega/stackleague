def translator(string):
    tempString = string.split()
    translated = []

    for word in tempString:
        translated.append(word[::-1])
    return ' '.join(translated)

print(translator('I  am  omega'))