def get_path(array):
    n = len(array)

    if array == [[]]:
        return []

    print(n)
    path = []
    top = 0
    bottom = n - 1
    left = 0
    right = n - 1
    direction = 0

    while (top <= bottom and left <= right):
        if direction == 0:
            for i in range(left, right + 1):
                path.append(array[top][i])
            top += 1
            direction = 1

        elif direction == 1:
            for i in range(top, bottom + 1):
                path.append(array[i][right])
            right -= 1
            direction = 2

        elif direction == 2:
            for i in range(right, left - 1, -1):
                path.append(array[bottom][i])
            bottom -= 1
            direction = 3

        elif direction == 3:
            for i in range(bottom, top - 1, -1):
                path.append(array[i][left])
            left += 1
            direction = 0
    return path

path = [[1,2,3,3],
        [4,5,6,5],
        [7,8,9,6],
        [1,2,3,7]]
print(get_path(path))
path = [[1]]
print(get_path(path))