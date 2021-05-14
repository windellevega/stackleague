def is_valid_rows(board):
    temp = []
    for x in range(9):
        for y in range(9):
            temp.append(board[x][y])

        if len(set(temp)) != 9:
            return False

    return True

def is_valid_columns(board):
    temp = []
    for x in range(9):
        for y in range(9):
            temp.append(board[y][x])

        if len(set(temp)) != 9:
            return False

    return True
def is_valid_grids(board):
    for gridstartx in [0, 3, 6]:
        for gridstarty in [0, 3, 6]:
            temp = []
            for x in range(gridstartx, gridstartx + 3):
                for y in range(gridstarty, gridstarty + 3):
                    temp.append(board[x][y])
            print(temp)
            if len(set(temp)) != 9:
                return False
    return True


def valid_sudoku_solution(board):
    print(is_valid_rows(board), is_valid_columns(board), is_valid_grids(board))
    if is_valid_rows(board) and is_valid_columns(board) and is_valid_grids(board):
        return True
    return False

import unittest

class MyTestCase(unittest.TestCase):
    def test___valid(self):
        board = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
                 [6, 7, 2, 1, 9, 5, 3, 4, 8],
                 [1, 9, 8, 3, 4, 2, 5, 6, 7],
                 [8, 5, 9, 7, 6, 1, 4, 2, 3],
                 [4, 2, 6, 8, 5, 3, 7, 9, 1],
                 [7, 1, 3, 9, 2, 4, 8, 5, 6],
                 [9, 6, 1, 5, 3, 7, 2, 8, 4],
                 [2, 8, 7, 4, 1, 9, 6, 3, 5],
                 [3, 4, 5, 2, 8, 6, 1, 7, 9]]
        self.assertEqual(valid_sudoku_solution(board), True)

    def test___invalid(self):
        board = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
                 [6, 7, 2, 1, 9, 5, 3, 4, 8],
                 [1, 9, 8, 3, 4, 2, 5, 6, 7],
                 [8, 5, 9, 7, 6, 1, 4, 2, 3],
                 [4, 2, 6, 8, 5, 3, 7, 9, 1],
                 [7, 1, 3, 9, 2, 4, 8, 5, 6],
                 [9, 6, 1, 5, 3, 7, 2, 8, 4],
                 [2, 8, 7, 4, 1, 9, 6, 3, 5],
                 [3, 4, 5, 2, 8, 6, 1, 7, 1]]
        self.assertEqual(valid_sudoku_solution(board), False)
if __name__ == '__main__':
    unittest.main()