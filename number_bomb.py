class NumberBomb:
    def get_sum_from_bomb(sequence, bomb, radius):
        lenSeq = len(sequence)
        for x in range(lenSeq):
            if sequence[x] == bomb:
                sequence[x] = 0
                for y in range(radius):
                    if x - y - 1 >= 0:
                        sequence[x - y - 1] = 0
                    if x + y + 1 < lenSeq:
                        sequence[x + y + 1] = 0

        return sum(sequence)


n = NumberBomb
print(n.get_sum_from_bomb([1, 2, 2, 4, 2, 2, 2, 9], 4, 2))
print(n.get_sum_from_bomb([1, 4, 4, 2, 8, 9, 1], 9, 3))