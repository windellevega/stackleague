from itertools import permutations
def next_bigger(number):

    # filter out number with same digits
    if str(number) == str(number)[0] * len(str(number)):
        return -1

    # filter out single digits
    if number < 10:
        return -1

    numbers = []

    # get number digit permutations
    for data in list(permutations(str(number))):
        if data[0] != '0':
            num = ''.join(data)
            numbers.append(int(num))

    # sort numbers
    numbers = sorted(set(numbers))
    print(numbers)
    # traverse and get next number
    for num in enumerate(numbers):
        if num[1] == number:
            if num[0] == len(numbers) - 1:
                return -1
            return numbers[num[0] + 1]

    return -1

def next_bigger1(number):
    num = list(str(number))

    index_to_swap = len(num) - 1

    for i in range(len(num) - 2, -1, -1):
        if num[i] < num[index_to_swap]:
            num[index_to_swap], num[i] = num[i], num[index_to_swap]
            return int(''.join(num))
            break
        else:
            index_to_swap = i
    else:
        return -1

print(next_bigger1(790))
# for x in range(99999):
#     print(next_bigger(x))