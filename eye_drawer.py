def draw_eye(value):
    # code here
    midPoints = value - 2
    sidePoints = value - 2 # -2 every line
    sideMidPoints = 0 # increased by 2 every line
    eye = ''

    eye += '.' * value + '#' * value + '.' * value + '\n'
    for ctr in range(value - 1):
        eye += '.' * sidePoints + '##' + '.' * sideMidPoints + '#' + '.' * midPoints + '#' + '.' * sideMidPoints + '##' + '.' * sidePoints + '\n'

        if ctr < (value - 3) / 2:
            sidePoints -= 2
            sideMidPoints += 2
        elif ctr > (value - 3) / 2:
            sidePoints += 2
            sideMidPoints -= 2
    eye += '.' * value + '#' * value + '.' * value

    return eye

print(draw_eye(15))