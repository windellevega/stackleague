from math import *


class GameMap:

    def __init__(self, width, height):
        # add code to set the width and height
        width = width if width >= 10 else 10
        height = height if height >= 10 else 10
        self.width = width
        self.height = height
        self.tiles = []
        for i in range(width):
            column = []
            for j in range(height):
                column.append(None)
            self.tiles.append(column)

    def place_unit(self, unit, x, y):
        if x >= self.width or y >= self.height:
            raise ValueError("Cannot do that")
        if self.tiles[x][y] is None:
            self.tiles[x][y] = unit
            unit.x = x
            unit.y = y
        else:
            raise ValueError("Cannot do that")

    def remove_unit(self, unit):
        self.tiles[unit.x][unit.y] = None

    def move_unit(self, unit, x, y):
        # this should move the unit to another tile
        # and update the unit's x and y coordinates
        if self.tiles[unit.x + x][unit.y + y] is None:
            self.tiles[unit.x + x][unit.y + y] = unit
            self.remove_unit(unit)
            unit.x += x
            unit.y += y
        else:
            raise ValueError("Cannot do that")

    def get_units_in_area(self, x, y, radius):
        # (x, y) serves as the central tile, radius
        # refers to how many tiles the area grows outwards
        a = max(0, x - radius)
        b = min(self.width - 1, x + radius)
        c = max(0, y - radius)
        d = min(self.height - 1, y + radius)
        units = []

        for idxy in range(c, d + 1):
            for idxx in range(a, b + 1):
                if self.tiles[idxx][idxy] is not None:
                    units.append(self.tiles[idxx][idxy])
        return units

    def end_turn(self):
        for idxy in range(self.height):
            for idxx in range(self.width):
                if self.tiles[idxx][idxy] is not None:
                    self.tiles[idxx][idxy].moves = 2


class Unit:

    def __init__(self, game_map, label):
        self.game_map = game_map
        self.x = 0
        self.y = 0
        self.health = 6
        self.moves = 2
        self.label = label

    def remove_self(self):
        self.game_map.remove_unit(self)

    def move(self, x_direction, y_direction):
        # x_direction and y_direction can have the following values: -1, 0, 1
        # the value given selects whether the unit will move backward, forward,
        # or stay in place along either the x or y axis
        # this function must call the move_unit() function of
        if self.moves > 0:
            self.game_map.move_unit(self, x_direction, y_direction)
            self.moves -= 1

    def shoot_unit(self, unit):
        if self.moves > 0:
            distance = self.get_distance_from_unit(unit)
            if distance <= 5 and not self.check_if_ally(unit):
                unit.take_damage((6 - distance) if distance > 1 else 6)
                if distance == 1:
                    unit.remove_self()
                self.moves = 0
            else:
                raise ValueError("Cannot do that")

    def get_distance_from_unit(self, unit):
        distance = sqrt(pow(unit.x - self.x, 2) + pow(unit.y - self.y, 2))
        return int(floor(distance))

    def check_if_ally(self, unit):
        return self.label == unit.label

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.remove_self()


class Soldier(Unit):

    def __init__(self, game_map):
        super(Soldier, self).__init__(game_map, "soldier")

    def throw_grenade(self, x, y):
        if self.moves > 0:
            a = max(0, x - 1)
            b = min(self.game_map.width-1, x + 1)
            c = max(0, y - 1)
            d = min(self.game_map.height-1, y + 1)

            for inity in range(c, d + 1):
                for initx in range(a, b + 1):
                    if initx == self.x and inity == self.y:
                        initx += 1
                    if self.game_map.tiles[initx][inity] is not None:
                        self.game_map.tiles[initx][inity].take_damage(3)
            self.moves = 0


class Alien(Unit):

    def __init__(self, game_map):
        super(Alien, self).__init__(game_map, "alien")

    def drain(self):
        if self.moves > 0:
            a = max(0, self.x - 2)
            b = min(self.game_map.width-1, self.x + 2)
            c = max(0, self.y - 2)
            d = min(self.game_map.height-1, self.y + 2)

            for inity in range(c, d + 1):
                for initx in range(a, b + 1):
                    if initx == self.x and inity == self.y:
                        initx += 1
                    if self.game_map.tiles[initx][inity] is not None:
                        self.game_map.tiles[initx][inity].take_damage(2)
                        self.health += 1
            self.moves = 0


game_map = GameMap(12, 12)
game_map.place_unit(Alien(game_map), 8, 8)
game_map.place_unit(Soldier(game_map), 9, 9)
alien = game_map.tiles[8][8]
# alien.move(1,2)
# print(alien.moves)
# print(alien.x, alien.y)
print(game_map.tiles[9][9].shoot_unit(alien)) # sqrt(3^2 + 3^) = 9 + 9
print(game_map.tiles[8][8])
# game_map = GameMap(10, 10)
# game_map.place_unit(Alien(game_map), 9, 1)
# game_map.place_unit(Soldier(game_map), 8, 1)
# alien = game_map.tiles[9][1]
# alien.drain()
# print(alien.health)
# print(game_map.tiles[8][1].health)
# #game_map.place_unit(Soldier(game_map), 2, 3)
# print(game_map.tiles)
# print(game_map.tiles[2][3])
# game_map.place_unit(Soldier(game_map), 4, 2)
# game_map.place_unit(Soldier(game_map), 5, 3)
# game_map.place_unit(Soldier(game_map), 6, 2)
# game_map.place_unit(Soldier(game_map), 3, 4)
# game_map.place_unit(Alien(game_map), 2, 2)
# game_map.place_unit(Alien(game_map), 3, 3)
# alien = game_map.tiles[2][3]

for idxy in range(game_map.height):
    for idxx in range(game_map.width):
        if game_map.tiles[idxx][idxy] is None:
            print("*", end=" ")
        elif game_map.tiles[idxx][idxy].label == "soldier":
            print("s", end=" ")
        else:
            print("a", end=" ")
    print("")

# for idxy in range(game_map.height):
#     for idxx in range(game_map.width):
#         print("*", end=" ")
#     print("")

# print(alien.x)
# print(alien.y)
# print(game_map.tiles[5][3].game_map)
# alien.move(0,0)
# print(alien.moves)
# soldier = game_map.tiles[6][2]
# soldier1 = game_map.tiles[3][4]
#
# print(alien.game_map.tiles[2][3])
# print(alien.game_map.tiles[3][3])
# print(len(alien.game_map.get_units_in_area(1, 1, 4)))
# print(alien.health)
# alien.drain()
# soldier.throw_grenade(3, 1)
# soldier1.shoot_unit(game_map.tiles[3][3])
# print(soldier.get_distance_from_unit(alien))  # sqrt((6-2)^2 + (2-3)^2) = sqrt(16+1) = 4....
# print(alien.health)
# # game_map.place_unit(Soldier(game_map), 2, 4)
# # game_map.place_unit(Soldier(game_map), 3, 3)
# # game_map.place_unit(Soldier(game_map), 4, 3)
# # game_map.place_unit(Soldier(game_map), 2, 5)
#
#
#
#
# print(game_map.tiles[1][1].health)
# print(game_map.tiles[4][2].health)
# print(game_map.tiles[5][3].health)
# print(game_map.tiles[6][2].health)
# print(game_map.tiles[3][4].health)
# print("")
# print(game_map.tiles[2][2].health)
# print(game_map.tiles[3][3].health)
# print(game_map.tiles[2][3].health)
# game_map.get_units_in_area(5, 5, 4)
# alien = game_map.tiles[2][3]
# soldier = game_map.tiles[2][4]
# soldier.throw_grenade(1, 1)
# alien.drain()
# print(alien.health)
# print(game_map.tiles[3][3].health)
