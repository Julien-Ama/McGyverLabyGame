import pygame
from BackSide.Map import Map
from configuration import config as CONFIG


class Visuel:

    def __init__(self):

        self.resolution = (750, 800)
        self.map = Map()

        pygame.init()
        pygame.display.set_caption("MacGyverTest")

        self.bleu_color = (89, 152, 255)
        self.white_color = (255, 255, 255)
        self.black_color = (0, 0, 0)
        self.screen = pygame.display.set_mode(self.resolution)
        print("En théorie, la fenêtre est créé et ouverte")
        self.green = (17, 179, 34)
        self.yellow = (187, 208, 12)
        # self.red1 = (49, 55, 17)
        self.red = (182, 24, 29)
        self.orange = (245, 121, 10)

        self.wall_image = pygame.image.load("ressource/mur.png")
        self.wall_image.convert()
        self.taille_mur = pygame.transform.scale(self.wall_image, (50, 50))

        self.mcgaver_image = pygame.image.load("ressource/mc2floor.png")
        self.mcgaver_image.convert()
        self.taille_mc = pygame.transform.scale(self.mcgaver_image, (50, 50))

        self.floor_image = pygame.image.load("ressource/floor.png")
        self.floor_image.convert()
        self.taille_floor = pygame.transform.scale(self.floor_image, (50, 50))

        self.gardien_image = pygame.image.load("ressource/Gardien.png")
        self.gardien_image.convert()
        self.taille_gardien = pygame.transform.scale(self.gardien_image,
                                                     (50, 50))

        self.aiguille_image = pygame.image.load("ressource/aiguille.png")
        self.aiguille_image.convert()
        self.taille_aiguille = pygame.transform.scale(self.aiguille_image,
                                                      (50, 50))

        self.tube_image = pygame.image.load("ressource/tube_plastique.png")
        self.tube_image.convert()
        self.taille_tube = pygame.transform.scale(self.tube_image, (50, 50))

        self.ether_image = pygame.image.load("ressource/ether.png")
        self.ether_image.convert()
        self.taille_ether = pygame.transform.scale(self.ether_image, (50, 50))

        self.ItemInv_image = pygame.image.load("ressource/itemInv.png")
        self.ItemInv_image.convert()
        self.taille_Inv = pygame.transform.scale(self.ItemInv_image, (30, 30))

        self.hero = pygame.display.update(self.screen.blit(self.taille_mc,
                                                           (50, 100)))

    def update(self, x, y, xPossibility, yPossibility):
        pygame.display.update(self.screen.blit(
            self.taille_mc, (yPossibility * 50, xPossibility * 50)))
        pygame.display.update(self.screen.blit(self.taille_floor,
                                               (y * 50, x * 50)))

    def lancement(self, pygame, map):

        launched = True

        while launched:

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    launched = False
                elif event.type == pygame.KEYDOWN:
                    launched = map.setMouvement(event.key, self)
        while not launched:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    launched = True

    def addAllObjectInWindowPygame(self, map):
        for x in range(0, 15):
            for y in range(0, 15):
                self.zero()
                print(x, y)
                pygame.display.flip()
                if map[x][y] is CONFIG.letterForWalls:
                    print("mur")
                    rect_form = pygame.Rect(y * 50, x * 50, (y + 1) * 50,
                                            (x + 1) * 50)
                    self.screen.blit(self.taille_mur, rect_form)
                elif map[x][y] is CONFIG.letterForSpace:
                    print("espace")
                    rect_form = pygame.Rect(y * 50, x * 50, (y + 1) * 50,
                                            (x + 1) * 50)
                    self.screen.blit(self.taille_floor, rect_form)
                elif map[x][y] is CONFIG.letterOfCharacter:
                    print("character")
                    rect_form = pygame.Rect(y * 50, x * 50, (y + 1) * 50,
                                            (x + 1) * 50)
                    self.screen.blit(self.taille_mc, rect_form)
                elif map[x][y] is CONFIG.letterForEnding:
                    print("fin")
                    rect_form = pygame.Rect(y * 50, x * 50, (y + 1) * 50,
                                            (x + 1) * 50)
                    self.screen.blit(self.taille_gardien, rect_form)
                elif map[x][y].isnumeric():
                    print("la numeriquevalue est : ", map[x][y])
                    if map[x][y] == "1":
                        rect_form = pygame.Rect(y * 50, x * 50, (y + 1) * 50,
                                                (x + 1) * 50)
                        self.screen.blit(self.taille_aiguille, rect_form)
                    elif map[x][y] == "2":
                        rect_form = pygame.Rect(y * 50, x * 50, (y + 1) * 50,
                                                (x + 1) * 50)
                        self.screen.blit(self.taille_tube, rect_form)
                    elif map[x][y] == "3":
                        rect_form = pygame.Rect(y * 50, x * 50, (y + 1) * 50,
                                                (x + 1) * 50)
                        self.screen.blit(self.taille_ether, rect_form)
                else:
                    print("une erreur se produit")

    def Victory(self):
        rect_form = pygame.Rect(300, 600, 50, 50)
        pygame.draw.rect(self.screen, self.black_color, rect_form)

        arial_font = pygame.font.SysFont("arial", 100)
        item_text = arial_font.render("VICTORY !", False, self.green)
        self.screen.blit(item_text, [125, 250])

        arial_font = pygame.font.SysFont("arial", 25)
        item_text = arial_font.render("you're finally free,"
                                      " but you're still single.",
                                      False, self.green)
        self.screen.blit(item_text, [150, 350])
        pygame.display.flip()

    def Defeat(self):
        self.screen.blit(self.taille_floor, (300, 550))

        arial_font = pygame.font.SysFont("arial", 100)
        item_text = arial_font.render("DEFEAT !", False, self.red)
        self.screen.blit(item_text, [150, 250])

        arial_font = pygame.font.SysFont("arial", 25)
        item_text = arial_font.render(
            "You must collect all the items before facing the keeper.",
            False, self.red)
        self.screen.blit(item_text, [70, 350])
        pygame.display.flip()

    def zero(self):
        arial_font = pygame.font.SysFont("arial", 30)
        item_text = arial_font.render("INVENTORY :", False, self.yellow)

        self.screen.blit(item_text, [5, 755])

        arial_font = pygame.font.SysFont("arial", 30)
        item_text = arial_font.render("[     .     .     ]", False, self.red)

        self.screen.blit(item_text, [200, 755])

        pygame.display.flip()

    def one(self):
        arial_font = pygame.font.SysFont("arial", 30)
        item_text = arial_font.render("[     .     .     ]", False, self.red)

        self.screen.blit(item_text, [200, 755])

        self.screen.blit(self.taille_Inv, (210, 760))
        pygame.display.flip()

    def two(self):
        arial_font = pygame.font.SysFont("arial", 30)
        item_text = arial_font.render("[     .     .     ]",
                                      False, self.orange)

        self.screen.blit(item_text, [200, 755])

        self.screen.blit(self.taille_Inv, (260, 760))
        pygame.display.flip()

    def max(self):
        arial_font = pygame.font.SysFont("arial", 30)
        item_text = arial_font.render("[     .     .     ]",
                                      False, self.green)

        self.screen.blit(item_text, [200, 755])

        self.screen.blit(self.taille_Inv, (310, 760))
        pygame.display.flip()
