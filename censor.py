import re
def censor(card_number: str) -> str:
    new_card_number = ""
    count_digit = 0
    if not re.match("^[\d\s]+$", card_number):
        return None

    # code here
    for str in enumerate(card_number) :
        if str[0] >= len(card_number) - 4 or str[1] == " ":
            new_card_number += str[1]
        else :
            new_card_number += "x"
        if str[1].isdigit():
            count_digit += 1

    if count_digit >= 13 and count_digit <= 19:
        return new_card_number

    return None
    pass

print(censor("676960 0000551045"))
print(censor("1234 2345 4567 13337"))
