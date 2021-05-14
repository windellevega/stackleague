import re
from itertools import islice
def is_sum_of_cubes(s):
    nums = ''.join(x if x.isnumeric() else ' ' for x in s)
    nums = nums.split()

    splitNums = []
    for x in range(len(nums)):
        if len(nums[x]) > 3:
            temp = []
            temp = [nums[x][i:i+3] for i in range(0, len(nums[x]), 3)]
            splitNums += temp
        else:
            splitNums.append(nums[x])
    nums = splitNums

    cubics = []
    sumCubics = 0
    for i in nums:
        if (is_cubic(i)):
            cubics.append(i)
            sumCubics += int(i)

    if len(cubics):
        return ' '.join(cubics) + ' ' + str(sumCubics) + ' ' + 'Lucky'

    return 'Unlucky'

def is_cubic(s):
    sum = 0
    for x in range(len(s)):
        sum += int(s[x]) ** 3

    return sum == int(s)

print(is_sum_of_cubes('0 9026315 -827&()'))
print(is_sum_of_cubes('aqdf& 0 1 xyz 153 777.777'))
print(is_sum_of_cubes('Once upon a midnight dreary, while100 I pondered, 9026315weak and weary -827&()'))