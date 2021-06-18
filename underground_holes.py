# A group of geologists are conducting an analysis of underground holes that might eventually cause
# sink holes. They usually conduct analysis on one large rectangular region of land at a time,
# they then create grid that divides the land into some square plots.
# Each plot is being analyzed by a sensing device to detect whether or not it has a hole underground.

# If two adjacent plots have holes under them, it means that they are part of one larger hole.
# As part of the group, you are to determine how many distinct large holes are contained in a grid.

# Note:
# - Holes under a plot is part of a larger hole if they are adjacent horizontally, vertically, or diagonally
# - Input grid would be an array strings that represent plots
# - Plot would be represented by either * for plot without hole under it and @ for plot with hole under.
# - Grid row and column sizes can be different but all elements that belong to the same row/column should have equal sizes
# - If grid is empty, return Error
# - If grid contains other characters, return Error

def underground_holes(grid):
    if (grid == []):
        raise ValueError

    m = len(grid)
    n = len(grid[0])

    for a in range(m):
        if(len(grid[a]) != n):
            raise ValueError

    def dfs(x, y):
        grid[x] = grid[x][:y] + '*' + grid[x][y+1:];

        for i in range(-1, 2):
            for j in range(-1, 2):
                dx = i + x
                dy = y + j

                if (dx >= 0 and dy >= 0 and dx < m and dy < n and grid[dx][dy] == '@'):
                    dfs(dx, dy)

    ans = 0;
    for i in range(m):
        for j in range(n):
            if(grid[i][j] == '@'):
                dfs(i, j)
                ans += 1
            elif(grid[i][j] != '@' and grid[i][j] != '*'):
                raise ValueError

    return ans

######################### END OF SOLUTION #########################





import unittest

class MyTestCase(unittest.TestCase):
    #SAMPLE TESTS
    def test___AL___sample_single_row_input(self):
        grid = ['@@****@*']

        self.assertEqual(underground_holes(grid), 2)

    def test___AL___sample_multiple_rows_input(self):
        grid = [
            '*****',
            '**@**',
            '*****']

        self.assertEqual(underground_holes(grid), 1)

    def test___AL___sample_multiple_larger_holes(self):
        grid = [
            '*****',
            '*@@**',
            '*@***',
            '*****',
            '**@@@']

        self.assertEqual(underground_holes(grid), 2)

    #TEST CASE
    def test___EH___empty_grid(self):
        with self.assertRaises(ValueError):
            grid = []
            underground_holes(grid)

    def test___EH___invalid_characters1(self):
        with self.assertRaises(ValueError):
            grid = [
                '****',
                '##**',
                '****']
            underground_holes(grid)

    def test___EH___invalid_characters2(self):
        with self.assertRaises(ValueError):
            grid = ['@@@***$*$*$']
            underground_holes(grid)

    def test___EH___invalid_characters2(self):
        with self.assertRaises(ValueError):
            grid = ['@@@***$*$*$']
            underground_holes(grid)

    def test___AL___single_plot1(self):
        grid = ['@']
        self.assertEqual(underground_holes(grid), 1)

    def test___AL___single_plot2(self):
        grid = ['*']
        self.assertEqual(underground_holes(grid), 0)

    def test___AL___multiple_larger_holes_1(self):
        grid = [
            '*******@@*****@@@@****@',
            '@@@****@**********@****',
            '@@@@***@*****@@@@@*****',
            '@@@@@@@@**********@@***',
            '@@********@@@******@***',
            '***************@*******',
            '********************@@@'
        ]
        self.assertEqual(underground_holes(grid), 6)

    def test___AL___multiple_larger_holes_2(self):
        grid = [
            '*******@@*****@@@@****@',
            '@@@****@**********@****',
            '@@@@*********@@@@@*****',
            '@@@**@@@**********@@***',
            '@@********@@@******@***',
            '***************@*******',
            '********************@@@'
        ]
        self.assertEqual(underground_holes(grid), 8)

    def test___AL___single_row(self):
        grid = [
            '*******@@*****@@@@****@'
        ]
        self.assertEqual(underground_holes(grid), 3)

    def test___AL___single_row2(self):
        grid = [
            '*@*@*@*@*@*@'
        ]
        self.assertEqual(underground_holes(grid), 6)

    def test___EH___irregular_grid_size(self):
        with self.assertRaises(ValueError):
            grid = [
                '*****',
                '****',
                '*****'
            ]
            underground_holes(grid)

if __name__ == '__main__':
    unittest.main()