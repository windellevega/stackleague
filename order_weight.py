import operator
def order_weight(string):
    numbers_split = string.split()
    numbers_with_sum = {}
    arranged_number_string = ""
    #print(numbers_split)
    numbers_split = sorted(numbers_split)
    for number in enumerate(numbers_split):
        temp_sum = 0;
        for digit in enumerate(number[1]):
            temp_sum += int(digit[1])
        #print(temp_sum)
        numbers_with_sum.update({number[0]:temp_sum})
    numbers_with_sum = sorted(numbers_with_sum.items(), key=operator.itemgetter(1))
    for item in numbers_with_sum:
        arranged_number_string += numbers_split[item[0]] + " "

    return arranged_number_string.rstrip()


print(order_weight("2000 10003 1234000 44444444 9999 11 11 22 123"))

#2,4,10,32,36,2,2,4,6