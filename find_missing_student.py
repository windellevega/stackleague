def find_missing_number(a):
    if a == []:
        return 1

    a = sorted(a)
    for stud in range(len(a)):
        if stud + 1 != a[stud]:
            return stud + 1
    return a[len(a) - 1] + 1

print(find_missing_number([2, 3, 4]))
print(find_missing_number([1, 3, 4]))
print(find_missing_number([1, 2, 3]))
print(find_missing_number([4, 2, 3]))
print(find_missing_number([]))