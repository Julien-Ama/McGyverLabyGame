import bcolors


class Character:
    objects = 0

    def __init__(self):
        self.x = 0
        self.y = 0

    def setCoordinates(self, newX, newY):
        self.x = newX
        self.y = newY
        print(bcolors.OKMSG + "Le personnage est en (",
              self.x, ",", self.y, ")")

    def moove(self, newX, newY):
        self.x = newX
        self.y = newY
        print(bcolors.OKMSG + "Le personnage est déplacé en (",
              self.x, ",", self.y, ")")

    def addObject(self):
        self.objects = self.objects + 1
