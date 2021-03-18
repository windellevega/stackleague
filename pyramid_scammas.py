class Person:
  def __init__(obj):
    obj.recruits = []
  def recruit (self, otherPerson):
    self.recruits.append(otherPerson)
  def getLoserCount (self):
    loser = 0
    if len(self.recruits) == 0:
        loser = 1

    for recruit in self.recruits:
        loser += recruit.getLoserCount()

    return loser
# top = level1, Person1, Person2
# leavel1 = level2a, level2b
# level2a = []
# level2b = []
top = Person()
level1 = Person()
level2a = Person()
level2b = Person()
level1.recruit(level2a)
level1.recruit(level2b)
top.recruit(level1)
top.recruit(Person())
top.recruit(Person())
print(top.getLoserCount())

top = Person()
print(top.getLoserCount())