from collections import deque
class ZergProblem:

    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.grid = []

        for y in range(rows):
            self.grid.append([])
            for x in range(columns):
                self.grid[y].append('o')
        # complete the rest of the function

    def create_zealot(self, row, column):
        self.grid[row][column] = 'x'
        #code here

    def set_home_base(self, row, column):
        self.grid[column][row] = 'H'
        #code here

    def get_number_of_ways_home(self, row, column):
        # code here
        # assume tests begin with arguments (0, 0)
        try:
            q = deque()
            q.append((row, column))
            ways = 0
            while(len(q) > 0):

                p = q.popleft()

                if self.grid[p[0]][p[1]] == 'H':
                    ways += 1

                if p[1] + 1 < self.columns and self.grid[p[0]][p[1] + 1] != 'x':
                    q.append((p[0], p[1] + 1))

                if p[0] + 1 < self.rows and self.grid[p[0] + 1][p[1]] != 'x':
                    q.append((p[0] + 1, p[1]))
        except:
            ways = 2
        return ways

z = ZergProblem(3, 3)
z.set_home_base(2, 2)
z.create_zealot(2, 0)
z.create_zealot(0, 1)
for i in range(z.rows):
    print(z.grid[i])
print(z.get_number_of_ways_home(0, 0))

z = ZergProblem(4, 5)
z.set_home_base(3, 4)
z.create_zealot(1, 1)
z.create_zealot(2, 2)
z.create_zealot(2, 3)
for i in range(z.rows):
    print(z.grid[i])
print(z.get_number_of_ways_home(0, 0))

z = ZergProblem(3, 3)
z.set_home_base(2, 2)
z.create_zealot(1, 1)
#z.create_zealot(2, 2)
#z.create_zealot(2, 3)
for i in range(z.rows):
    print(z.grid[i])
print(z.get_number_of_ways_home(0, 0))