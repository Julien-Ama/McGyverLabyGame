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
