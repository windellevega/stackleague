import math
import itertools
import re
import operator
import collections


class Room:

    def __init__(self, potion):
        self.next_room = None
        self.enemy = None
        self.potion = potion if potion is not None else None

    def set_next_room(self, next_room):
        self.next_room = next_room

    def get_next_room(self):
        return self.next_room

    def get_potion(self):
        return self.potion

    def remove_potion(self):
        self.potion = None

    def get_enemy(self):
        return self.enemy

    def set_enemy(self, enemy):
        self.enemy = enemy

    def enemy_alive(self):
        # return boolean: check if enemy in room exists and is alive
        pass


class Unit:

    def __init__(self, current_room, health, damage):
        self.current_room = current_room
        self.current_hp = health
        self.damage = damage

    def get_current_room(self):
        return self.current_room

    def set_current_room(self, room):
        self.current_room = room

    def get_health(self):
        return self.current_hp

    def set_health(self, value):
        self.current_hp = value

    def decrease_health(self, value):
        # inherited by Player to affect ability to act
        self.current_hp -= value

    def get_damage(self):
        return self.damage


class Player(Unit):

    def __init__(self, initial_room, health, damage):
        super().__init__(initial_room, health, damage)
        self.max_hp = health
        self.previous_room = None
        self.invisibility = 0
        self.shielded = True
        self.can_act = True
        self.backpack = [None, None, None]

    def decrease_health(self, value):
        # inherited by Player to affect ability to act
        super().decrease_health(value)

    def increase_health(self, value):
        if self.can_act:
            super().set_health(super().get_health() + value)

    def advance(self):
        enemy = super().get_current_room().get_enemy()
        if (enemy == None or enemy.get_health() <= 0 or self.invisibility > 0) and self.can_act:
            if enemy == None and self.invisibility > 0:
                self.invisibility -= 1
            elif enemy != None and enemy.get_health() > 0 and self.invisibility > 0:
                self.invisibility = 0

            # advances Player to next room
            curr_room = super().get_current_room()

            if(curr_room.get_next_room() == None):
                self.can_act = False
            else:
                self.previous_room = curr_room
                super().set_current_room(curr_room.get_next_room())

    def attack_enemy(self):
        # Player attacks enemy Unit in current_room if it exists or is alive
        self.invisibility = 0

        curr_room = super().get_current_room()
        enemy = curr_room.get_enemy()

        if self.can_act and enemy != None and enemy.get_health() >= 0:
            enemy.decrease_health(super().get_damage())
            self.decrease_health(enemy.get_damage())

            if super().get_health() <= 0 and self.shielded == True:
                super().set_current_room(self.previous_room)
                super().set_health(1)
                self.shielded = False
                self.previous_room = None

            if super().get_health() <= 0 and self.shielded == False:
                self.can_act = False

    def pick_up_potion(self):
        curr_room = super().get_current_room()

        if curr_room.get_potion() != None and self.can_act:
            if self.backpack[2] == None:
                for i in range(1, -1, -1):
                    self.backpack[i + 1] = self.backpack[i]

                curr_room.get_potion().set_user(self)
                self.backpack[0] = curr_room.get_potion()
                curr_room.remove_potion()

    def use_potion(self):
        # call the use() function of first Potion in backpack
        if self.can_act and self.backpack[0] != None:
            self.backpack[0].use()
            for i in range(2):
                self.backpack[i] = self.backpack[i+1]

            self.backpack[2] = None

            if self.max_hp < super().get_health():
                super().set_health(self.max_hp)

    def shield(self):
        if self.can_act:
            self.shielded = True

    def go_invisible(self):
        if self.can_act:
            self.invisibility = 2

    def get_backpack(self):
        # for testing purposes do not remove
        return self.backpack


class Potion:

    def Potion(self):
        self.user = None

    def get_user(self):
        return self.user

    def set_user(self, user):
        self.user = user


class HealthPotion(Potion):

    def __init__(self, value):
        super().__init__()
        self.value = value

    def use(self):
        super().get_user().increase_health(self.value)


class InvisibilityPotion(Potion):

    def use(self):
        super().get_user().go_invisible()


class ShieldPotion(Potion):

    def use(self):
        super().get_user().shield()

######################### END OF SOLUTION #########################





import unittest

class MyTestCase(unittest.TestCase):
    def test___OO___advance(self):
        first = Room(None)
        second = Room(None)
        first.set_next_room(second)
        player = Player(first, 1, 1)
        player.advance()
        self.assertEqual(player.get_current_room(), second)

    def test___OO___attack_player_hp(self):
        first = Room(None)
        second = Room(None)
        first.set_next_room(second)
        second.set_enemy(Unit(second, 5, 1))
        player = Player(first, 5, 1)
        player.advance()
        player.attack_enemy()
        self.assertEqual(player.get_health(), 4)

    def test___OO___attack_enemy_hp(self):
        first = Room(None)
        second = Room(None)
        first.set_next_room(second)
        second.set_enemy(Unit(second, 5, 1))
        player = Player(first, 5, 1)
        player.advance()
        player.attack_enemy()
        self.assertEqual(second.get_enemy().get_health(), 4)

    def test___OO___use_invisibility_potion(self):
        first = Room(InvisibilityPotion())
        second = Room(None)
        third = Room(None)
        fourth = Room(None)
        first.set_next_room(second)
        second.set_next_room(third)
        third.set_next_room(fourth)
        #second.set_enemy(Unit(second, 5, 1))
        player = Player(first, 5, 1)
        player.pick_up_potion()
        player.advance()
        player.use_potion()
        player.advance()
        self.assertEqual(player.invisibility, 1)

    def test___OO___pick_up_potion(self):
        first = Room(None)
        second = Room(HealthPotion(1))
        first.set_next_room(second)
        player = Player(first, 1, 1)
        player.advance()
        player.pick_up_potion()
        self.assertTrue(second.get_potion() == None)

    def test___OO___put_potion_in_backpack(self):
        first = Room(None)
        second = Room(HealthPotion(1))
        first.set_next_room(second)
        player = Player(first, 1, 1)
        player.advance()
        player.pick_up_potion()
        self.assertTrue(player.get_backpack()[0] != None)

    def test___OO___use_health_potion(self):
        first = Room(None)
        second = Room(HealthPotion(3))
        first.set_next_room(second)
        second.set_enemy(Unit(second, 5, 1))
        player = Player(first, 5, 1)
        player.advance()
        player.pick_up_potion()
        player.attack_enemy()
        player.use_potion()
        self.assertEqual(player.get_health(), 5)

    def test___OO___potions_full(self):
        first = Room(HealthPotion(1))
        second = Room(HealthPotion(1))
        third = Room(HealthPotion(1))
        fourth = Room(HealthPotion(1))
        first.set_next_room(second)
        second.set_next_room(third)
        third.set_next_room(fourth)
        player = Player(first, 1, 1)
        player.pick_up_potion()
        player.advance()
        player.pick_up_potion()
        player.advance()
        player.pick_up_potion()
        player.advance()
        player.pick_up_potion()
        self.assertTrue(fourth.get_potion() != None)

if __name__ == '__main__':
    unittest.main()