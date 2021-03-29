def wildWest(directions):
    opposites = ['NORTH,SOUTH', 'SOUTH,NORTH', 'WEST,EAST', 'EAST,WEST', 'NORTH, SOUTH', 'SOUTH, NORTH', 'WEST, EAST', 'EAST, WEST']

    directions = ','.join(directions)
    directions = directions.upper()
    print(directions)
   # print(directions)

    while True:
        directions = directions.replace(',,', ',')
        check = 0
        for opposite in opposites:
            if opposite in directions:
                directions = directions.replace(opposite,'')
                directions = directions.replace(',,', ',')
                check += 1

        if check == 0:
            #print(directions)
            directions = directions.rstrip(',')
            directions = directions.lstrip(',')
            if directions == '':
                return []
            return directions.split(',')

print(wildWest(["nORTh", "SoUTH", "EAsT", "wEST"]))
print(wildWest(["NORTH", "EAST", "SOUTH", "WEST"]))
print(wildWest(["NorTH", "EAsT", "soUTH", "NORTH", "WEST"]))
print(wildWest(['NORTH', 'EAST', 'NORTH', '', 'SOUTH']))