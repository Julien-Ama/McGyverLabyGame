from BackSide import Map
from FrontSide import Visuel
import pygame


class Engine:

    def __init__(self):
        myMap = Map()
        myVisuel = Visuel()
        myVisuel.addAllObjectInWindowPygame(myMap.map)
        myVisuel.lancement(pygame, myMap)
        myVisuel.one()
        play = True
        # while play:
        #     keyPressed = input("Choississez un déplacement :\n")
        #     play = myMap.setMouvement(keyPressed)
