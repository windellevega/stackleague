def wave(str):
    waves = []
    for char in enumerate(str):
        if(char[1].isalpha()):
            temp = list(str)
            temp[char[0]] = char[1].upper()
            waves.append(''.join(temp))

    return waves


wave(' asdasd ')