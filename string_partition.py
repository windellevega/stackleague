class StringPartition:

    def __init__(self, strings):
        self.strings = strings

    def merge(self, start_index, end_index):
        result = []
        tempStr = ''
        if start_index < 0:
            start_index = 0
        if end_index >= len(self.strings):
            end_index = len(self.strings) - 1

        for x in range(0, len(self.strings)):
            if x >= start_index and x <= end_index:
                tempStr += self.strings[x]
            if x == end_index:
                result.append(tempStr)
            if x < start_index or x > end_index:
                result.append(self.strings[x])

        self.strings = result
        return self.strings

    def divide(self, index, partitions):
        result = []

        for x in range(0, len(self.strings)):
            if x == index:
                n = int(len(self.strings[x]) / partitions)
                ctr = 1
                for y in range(0, len(self.strings[x]), n):
                    if ctr == partitions:
                        result.append(self.strings[x][y:len(self.strings[x])])
                        break
                    else:
                        result.append(self.strings[x][y:y + n])
                    ctr += 1
            else:
                result.append(self.strings[x])

        self.strings = result
        return self.strings

    def get_string_representation(self):
        # do not remove; for testing

        representation = ""

        for i in range(0, len(self.strings)):
            representation += self.strings[i] + " "

        return representation

s = StringPartition(["abc", "def", "ghi"])
print(s.merge(0, 1))
s = StringPartition(["zx", "cx", "bv"])
print(s.merge(-1, 3))
s = StringPartition(["abcd", "efgh", "ijkl"])
print(s.merge(1, 2))
s = StringPartition(["abc", "def", "ghi"])
print(s.divide(0, 3))
s = StringPartition(["yuiop", "ksj", "gkl"])
print(s.divide(0, 2))
s = StringPartition(["abcd", "efgh", "ijkl"])
print(s.divide(0, 3))
s = StringPartition(["abcd", "efgh", "ijkl", "mnop", "qrst", "uvwx", "yz"])
print(s.merge(4, 10))
print(s.divide(4, 5))