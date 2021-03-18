def send_message(s):
    keypad = {
        '1' : ['.', ',', '?', '!'],
        '2' : ['a', 'b', 'c'],
        '3' : ['d', 'e', 'f'],
        '4' : ['g', 'h', 'i'],
        '5' : ['j', 'k', 'l'],
        '6' : ['m', 'n', 'o'],
        '7' : ['p', 'q', 'r', 's'],
        '8' : ['t', 'u', 'v'],
        '9' : ['w', 'x', 'y', 'z'],
        '*' : ['\'', '-', '+', '='],
        '0' : [' ']
    }

    toggleCaps = 0
    strCode = ''
    tempKey = ''

    for char in s:
        if char == '#':
            strCode += '#-'
        else:
            for items in keypad:
                ctr = 0
                if char == items and tempKey == items:
                    strCode += ' ' + items + '-'
                    tempKey = ''
                elif char == items:
                    strCode += items + '-'
                    tempKey = ''
                for keyChar in keypad[items]:
                    ctr += 1

                    if char.lower() == keyChar:
                        if toggleCaps == 0 and char.isupper():
                            strCode += '#'
                            toggleCaps = abs(toggleCaps - 1)
                        elif toggleCaps == 1 and char.islower():
                            strCode += '#'
                            toggleCaps = abs(toggleCaps - 1)
                        elif tempKey == items:
                            strCode += ' '

                        tempKey = items
                        strCode += items * ctr

    return strCode

print(send_message("a"))
print(send_message("z"))
print(send_message("?"))
print(send_message("+"))
print(send_message("0011**##"))
print(send_message("Az"))
print(send_message("a7BK"))
print(send_message("hihibC"))
print(send_message("4g"))
print(send_message("Jk"))
print(send_message("Def Con 0 1!!'"))
print(send_message("  0aaab2a"))
print(send_message("2a1."))
