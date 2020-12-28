from BackSide.Map import Map
from FrontSide.Visuel import Visuel
import pygame


class Engine:

    def __init__(self):
        myMap = Map()
        myVisuel = Visuel()
        myVisuel.addAllObjectInWindowPygame(myMap.map)
        myVisuel.lancement(pygame, myMap)
        myVisuel.one()
