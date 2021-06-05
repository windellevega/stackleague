import math
import itertools
import re
import operator
import collections

def check_word(board, word):
    grid = [l + [''] for l in board] + [[''] * (len(board[0]) + 1)]
    def rc(x, y, i):
        if i == len(word):
            return True
        if grid[x][y] != word[i]:
            return False

        grid[x][y] = ''

        r = any(rc(x + u, y + v, i + 1)
                for u in range(-1, 2)
                for v in range(-1, 2))

        grid[x][y] = word[i]
        return r

    return any(rc(x, y, 0)
               for x in range(len(board))
               for y in range(len(board[x])))

import unittest

class MyTestCase(unittest.TestCase):
    def test_1(self):
        testBoard = [
            ["E", "A", "R", "A"],
            ["N", "L", "E", "C"],
            ["I", "A", "I", "S"],
            ["B", "Y", "O", "R"]
        ]

        self.assertEqual(check_word(testBoard, "C"), True)

    def test_2(self):
        testBoard = [
            ["E", "A", "R", "A"],
            ["N", "L", "E", "C"],
            ["I", "A", "I", "S"],
            ["B", "Y", "O", "R"]
        ]

        self.assertEqual(check_word(testBoard, "C"), True)

    def test_3(self):
        testBoard = [
            ["E", "A", "R", "A"],
            ["N", "L", "E", "C"],
            ["I", "A", "I", "S"],
            ["B", "Y", "O", "R"]
        ]

        self.assertEqual(check_word(testBoard, "EAR"), True)

    def test_4(self):
        testBoard = [
            ["E", "A", "R", "A"],
            ["N", "L", "E", "C"],
            ["I", "A", "I", "S"],
            ["B", "Y", "O", "R"]
        ]

        self.assertEqual(check_word(testBoard, "EARS"), False)

    def test_5(self):
        testBoard = [
            ["E", "A", "R", "A"],
            ["N", "L", "E", "C"],
            ["I", "A", "I", "S"],
            ["B", "Y", "O", "R"]
        ]

        self.assertEqual(check_word(testBoard, "BAILER"), True)

    def test_6(self):
        testBoard = [
            ["E", "A", "R", "A"],
            ["N", "L", "E", "C"],
            ["I", "A", "I", "S"],
            ["B", "Y", "O", "R"]
        ]

        self.assertEqual(check_word(testBoard, "RSCAREIOYBAILNEA"), True)

    def test_7(self):
        testBoard = [
            ["E", "A", "R", "A"],
            ["N", "L", "E", "C"],
            ["I", "A", "I", "S"],
            ["B", "Y", "O", "R"]
        ]

        self.assertEqual(check_word(testBoard, "CEREAL"), False)

    def test_8(self):
        testBoard = [
            ["E", "A", "R", "A"],
            ["N", "L", "E", "C"],
            ["I", "A", "I", "S"],
            ["B", "Y", "O", "R"]
        ]

        self.assertEqual(check_word(testBoard, "ROBES"), False)

if __name__ == '__main__':
    unittest.main()