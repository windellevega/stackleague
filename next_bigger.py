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


print(next_bigger(5988889853))
# for x in range(99999):
#     print(next_bigger(x))