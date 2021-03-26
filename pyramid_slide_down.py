def pyramid_slide_down(pyramid):
    if len(pyramid) == 1:
        return pyramid[0][0]

    last_layer = pyramid[-1]
    add_layer = []

    for i in range(1, len(last_layer)):
        add_layer.append(max(last_layer[i], last_layer[i - 1]))

    pyramid[-2] = [a + b for a, b in zip(pyramid[-2], add_layer)]

    return pyramid_slide_down(pyramid[:-1])

pyramid = [[15], [5, 8],  [3, 4, 1]]
print(pyramid_slide_down(pyramid))
pyramid = [[75], [95, 64], [17, 47, 82], [18, 35, 87, 10]]
print(pyramid_slide_down(pyramid))