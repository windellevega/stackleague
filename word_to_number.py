import  re
def word_to_number(string):
    string = string.lower()
    numwords = {}

    # singles
    units = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen",
    ]

    # tens
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    # larger scales
    scales = ["hundred", "thousand", "million", "billion", "trillion"]

    tempCheck = string.split(' ')
    for temp in tempCheck:
        temp = temp.split('-');
        if len(temp) > 2 or (len(temp) == 2 and temp[0] not in tens):
            return "Input not a string"

    # divisors
    numwords["and"] = (1, 0)

    # perform our loops and start the swap
    for idx, word in enumerate(units):    numwords[word] = (1, idx)
    for idx, word in enumerate(tens):     numwords[word] = (1, idx * 10)
    for idx, word in enumerate(scales):   numwords[word] = (10 ** (idx * 3 or 2), 0)

    # primary loop
    current = result = 0
    # loop while splitting to break into individual words
    for word in string.replace("-", " ").split():
        # if problem then fail-safe
        if word not in numwords:
            return "Input not a string"

        # use the index by the multiplier
        scale, increment = numwords[word]
        current = current * scale + increment

        # if larger than 100 then push for a round 2
        if scale > 100:
            result += current
            current = 0

    # return the result plus the current
    return result + current

words = 'one hundred fifty-six thousand and Five'
words = words.split(',')

for word in words:
    print(word_to_number(word))
