import random
from configuration import *
import bcolors as bcolors
from BackSide import Character
import pygame


class Map:

    def __init__(self):
        self.character = Character()
        self.map = []
        with open(configFile) as f:
            line = True
            while line:
                line = f.readline()
                if line:
                    line = line.replace("\n", "")
                    self.map.insert(len(self.map), list(line))
        self.setCharacter()
        self.addObjects()

    def setCharacter(self):
        for x in range(15):
            for y in range(15):
                if self.map[x][y] is letterOfCharacter:
                    self.character.setCoordinates(x, y)

    def addObjects(self):
        allPossibilitiesForObjects = []
        for x in range(15):
            for y in range(15):
                if self.map[x][y] is letterForSpace:
                    allPossibilitiesForObjects.insert(len(allPossibilitiesForObjects) - 1, (x, y))

        maxObjects = 3
        if len(allPossibilitiesForObjects) < 3:
            print("Il n'y a pas assez de place sur la carte pour poser des objets.")
            print("Veuillez vérifier la configuration de votre carte.")
            return False
        for objects in range(1, maxObjects + 1):
            allPossibilitiesForObjectsCount = len(allPossibilitiesForObjects) - 1
            randomPosition = random.randint(0, allPossibilitiesForObjectsCount)
            randomCoordinates = allPossibilitiesForObjects[randomPosition]
            randomX = randomCoordinates[0]
            randomY = randomCoordinates[1]
            self.map[randomX][randomY] = str(objects)
            allPossibilitiesForObjects.remove(randomCoordinates)
        print(bcolors.OK + "Les objets sont posés sur la carte !")
        self.displayMap()

    def displayMap(self):
        print(bcolors.FAIL + "\n-----------------------------")
        for x in range(15):
            for y in range(15):
                if self.map[x][y] is letterForSpace:
                    print(bcolors.BLUE + self.map[x][y], end=" ")
                elif self.map[x][y] is letterOfCharacter:
                    print(bcolors.WARN + self.map[x][y], end=" ")
                elif self.map[x][y] is letterForWalls:
                    print(bcolors.FAIL + self.map[x][y], end=" ")
                else:
                    print(bcolors.PASS + self.map[x][y], end=" ")
            print("\n")
        print(bcolors.FAIL + "-----------------------------\n")

    def setMouvement(self, inputType, visuel):
        x = self.character.x
        y = self.character.y

        inputMove = {
            pygame.K_UP: {
                'x': -1,
                'y': 0
            },
            pygame.K_DOWN: {
                'x': 1,
                'y': 0
            },
            pygame.K_LEFT: {
                'x': 0,
                'y': -1
            },
            pygame.K_RIGHT: {
                'x': 0,
                'y': 1
            }
        }
        if inputType in inputMove:
            return self.doMoovement(x + inputMove[inputType]['x'], y + inputMove[inputType]['y'], visuel)
        else:
            print(bcolors.FAIL + "Commande non reconnue")
            return False

    # noinspection PyUnresolvedReferences
    def doMoovement(self, xPossibility, yPossibility, visuel):
        """
        Args:
            xPossibility:
            yPossibility:
        Returns:
        """
        x = self.character.x
        y = self.character.y
        if self.checkCoordinates(xPossibility, yPossibility):
            if self.map[xPossibility][yPossibility] is not letterForWalls:
                # visuel.mst()
                if self.map[xPossibility][yPossibility].isnumeric() > 0:
                    self.character.addObject()
                if self.map[xPossibility][yPossibility] is letterForEnding:
                    print("vous êtes a la fin !")
                    if self.character.objects is maxObjects:
                        print(" Vous avez gagné !")
                        visuel.Victory()
                    else:
                        print(" Vous êtes mort !")
                        visuel.Defeat()
                    return False

                self.character.moove(xPossibility, yPossibility)
                self.map[x][y] = letterForSpace
                self.map[xPossibility][yPossibility] = letterOfCharacter
                # ici on doit faire l'update de pygame ( xPossility, yPossibility, x, y)
                visuel.update(x, y, xPossibility, yPossibility)
            else:
                print(bcolors.WARN + "Vous ne pouvez pas aller par ici, il y a un mur !")
        self.displayMap()
        print("Le personnage possède", self.character.objects, "objets")
        if self.character.objects is oneObjects:
            visuel.one()
        if self.character.objects is twoObjects:
            visuel.two()
        if self.character.objects is maxObjects:
            visuel.max()
        return True

    @staticmethod
    def checkCoordinates(x, y):
        """
        Args:
            x: Coordonnées de X
            y: Coordonnées de Y
        Returns: Boolean (Si les coordonnées sont toujours dans le labyrinthe ou pas)
        """
        if x < minX or x > maxX:
            return False
        if y < minY or y > maxY:
            return False
        return True
