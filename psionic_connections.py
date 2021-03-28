class ProtossProblem:

    def __init__(self, zealot_grid):
        self.zealot_grid = zealot_grid
        # this should be an array of arrays of "Y"s and "N"s
        # add any necessary code here

    def get_most_hyper_connections(self):
        connections = []
        highest = 0
        for zeal in range(len(self.zealot_grid)):
            connections.append([]);
        for zealot in enumerate(self.zealot_grid):
            for conn in enumerate(zealot[1]):
                if self.zealot_grid[zealot[0]][conn[0]] == "Y" and self.zealot_grid[conn[0]][zealot[0]] == "Y" and zealot[0] != conn[0]:
                    connections[zealot[0]].append(conn[0])

        for conn in enumerate(connections):
            temp = {}
            for cn in enumerate(conn[1]):
                temp = set(conn[1] + connections[cn[1]])
            if len(temp) - 1 > highest:
                highest = len(temp) - 1
            print(temp)
        print(connections)
        return highest

p = ProtossProblem([["N", "Y", "Y"],
                    ["Y", "N", "Y"],
                    ["Y", "Y", "N"]])
print(p.get_most_hyper_connections())
p = ProtossProblem([["N", "Y", "N"],
                    ["Y", "N", "N"],
                    ["N", "Y", "N"]])
print(p.get_most_hyper_connections())
p = ProtossProblem([["N", "Y", "N", "Y", "Y"],
                    ["Y", "N", "Y", "N", "Y"],
                    ["N", "Y", "N", "N", "Y"],
                    ["Y", "N", "Y", "N", "Y"],
                    ["Y", "N", "Y", "N", "Y"]])
print(p.get_most_hyper_connections())