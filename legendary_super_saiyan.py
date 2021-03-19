class Saiyan():

    def __init__(self):
        self._experience = 100
        self._level = 1
        self.rs = ["False Super Saiyan", "Super Saiyan", "SSG2", "SSG3", "SS Full Power", "SSJ2", "SSJ3", "SSJ4",
                   "SSJ rage", "Super Saiyan God", "SSJ Blue"]
        self.achievements = []

    def training(self, train): #train[0] = desc, train[1] = exp pts, train[2] = min lvl
        # code here
        if self._level < train[2]:
            return "Not strong enough"

        self.achievements.append(train[0])
        self._experience += train[1]
        self._level = int(self._experience / 100)
        return train[0]

    def battle(self, lvl):
        # code here
        leveldiff = lvl - self._level
        if not lvl >= 1 and lvl <= 100:
            return "Invalid level"

        if leveldiff >= 5:
            return "You've been defeated"
        elif leveldiff == 0:
            self._experience += 10
            self._level = int(self._experience / 100)
            return "A good fight"
        elif leveldiff == -1:
            self._experience += 5
            self._level = int(self._experience / 100)
            return "A good fight"
        elif leveldiff <= -2:
            self._experience += 0
            self._level = int(self._experience / 100)
            return "Easy fight"
        elif leveldiff >= 1:
            self._experience += 20 * leveldiff * leveldiff
            self._level = int(self._experience / 100)
            return "An intense fight"

        pass

    def specialBattle(self, specialEnemy):
        # code here
        leveldiff = specialEnemy.level - self._level
        if not specialEnemy.level >= 1 and specialEnemy.level <= 100:
            return  "Invalid level"

        if leveldiff >= 5:
            return  "You've been defeated"
        elif leveldiff == 0:
            self._experience += 10
            self._level = int(self._experience / 100)
            return  "Killed " + specialEnemy.name
        elif leveldiff == -1:
            self._experience += 5
            self._level = int(self._experience / 100)
            return  "Killed " + specialEnemy.name
        elif leveldiff <= -2:
            self._experience += 0
            self._level = int(self._experience / 100)
            return  "Killed " + specialEnemy.name
        elif leveldiff >= 1:
            self._experience += 20 * leveldiff * leveldiff
            self._level = int(self._experience / 100)
            return  "Killed " + specialEnemy.name
        pass

    @property
    def level(self):
        # code here
        return self._level

    @property
    def rank(self):
        return self.rs[int(self._level/10)]

    @property
    def experience(self):
        return self._experience;

class Bad_saiyan():
    name = ""
    level = 0
    rank = ""

    def __init__(self, name, level, rank):
        # code here
        self.name = name
        self.level = level
        self.rank = rank
        pass
