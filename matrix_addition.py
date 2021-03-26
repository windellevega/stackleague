def matrix_addition(a, b):
    sum = []
    for row in enumerate(a):
        for col in enumerate(row[1]):
            a[row[0]][col[0]] += b[row[0]][col[0]]

    return a


print(matrix_addition([[1, 2],[1, 2]], [[2, 3],[2, 3]]))