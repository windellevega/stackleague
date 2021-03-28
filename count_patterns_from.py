def count_patterns_from(firstPoint, length):
    pattern = {
        'A' : ['B', 'D', 'E', 'F', 'H'],
        'B' : ['A', 'C', 'D', 'E', 'F', 'G', 'I'],
        'C' : ['B', 'D', 'E', 'F', 'H'],
        'D' : ['A', 'B', 'C', 'E', 'G', 'H', 'I'],
        'E' : ['A', 'B', 'C', 'D', 'F', 'G', 'H', 'I'],
        'F' : ['A', 'B', 'C', 'E', 'G', 'H', 'I'],
        'G' : ['B', 'D', 'E', 'F', 'H'],
        'H' : ['A', 'C', 'D', 'E', 'F', 'G', 'I'],
        'I' : ['B', 'D', 'E', 'F', 'H']
    }

    patternEx = {
        'A' : ['C', 'G', 'I'],
        'B' : ['H'],
        'C' : ['A', 'G', 'I'],
        'D' : ['F'],
        'F' : ['D'],
        'G' : ['A', 'C', 'I'],
        'H' : ['B'],
        'I' : ['A', 'C', 'G']
    }
    vals = []
    if length == 0 or length == 10:
        return 0

count_patterns_from('A',10)