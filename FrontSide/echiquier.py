# import itertools
# import pygame as pg
# "les modules ???"
#
# pg.init()
# "les couleurs ????"
# BLACK = pg.Color('black')
# WHITE = pg.Color('white')
# "Pourquoi les doubles parentheses ???"
# resolution = (750, 750)
# screen = pg.display.set_mode(resolution)
# clock = pg.time.Clock()
#
# colors = itertools.cycle((WHITE, BLACK))
# tile_size = 50
# "width est non metrisable ???"
# width, height = 15*tile_size, 15*tile_size
# background = pg.Surface((width, height))
#
# for y in range(0, height, tile_size):
#     for x in range(0, width, tile_size):
#      rect = (x, y, tile_size, tile_size)
#      pg.draw.rect(background, next(colors), rect)
#
#
# game_exit = False
# while not game_exit:
#     for event in pg.event.get():
#      if event.type == pg.QUIT:
#       game_exit = True
#
#     screen.fill((60, 70, 90))
#     screen.blit(background, (0, 0))
#
#     pg.display.flip()
#     clock.tick(50)
#
# pg.quit()
# toto = (4,3)
#
# """""""""""
#
# import pygame
# from macGyverVersionFinale.BackSide import Map
# from macGyverVersionFinale.configuration import *
#
#
#
# class Visuel:
#
#     def __init__(self):
#
#         pygame.init()
#
#         resolution = (750, 750)
#
#         pygame.init()
#         pygame.display.set_caption("MacGyverTest")
#         self.black_color = (89, 152, 255)
#         self.white_color = (0, 0, 0)
#         self.screen = pygame.display.set_mode(resolution)
#
#
#
#
#
#
#         print("En théorie, la fenêtre est créé et ouverte")
#
#
#
#
#
#     def lancement(self, pygame):
#
#
#         launched = True
#
#         while launched:
#
#             "screen.blit(background, (500,300))"
#
#
#
#             pygame.display.flip()
#
#
#
#
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     launched = False
#
#
#
#
#
#     def addAllObjectInWindowPygame(self, map):
#         for x in range(0, 15):
#             for y in range(0, 15):
#                 numericValue = map[x][y].isnumeric()
#                 if map[x][y] is letterForWalls:
#                     rect_form = pygame.Rect(x * 50, y * 50, (x + 1) * 50, (y + 1) * 50)
#                     pygame.draw.rect(self.screen, self.black_color, rect_form)
#                 elif map[x][y] is letterForSpace:
#                     rect_form = pygame.Rect(x * 50, y * 50, (x + 1) * 50, (y + 1) * 50)
#                     pygame.draw.rect(self.screen, self.white_color, rect_form)
#                 elif map[x][y] is letterOfCharacter:
#                     rect_form = pygame.Rect(x * 50, y * 50, (x + 1) * 50, (y + 1) * 50)
#                     pygame.draw.rect(self.screen, self.white_color, rect_form)
#                 elif map[x][y] is letterForEnding:
#                     rect_form = pygame.Rect(x * 50, y * 50, (x + 1) * 50, (y + 1) * 50)
#                     pygame.draw.rect(self.screen, self.white_color, rect_form)
#                 elif numericValue > 0:
#                     if numericValue == 1:
#                         rect_form = pygame.Rect(x * 50, y * 50, (x + 1) * 50, (y + 1) * 50)
#                         pygame.draw.rect(self.screen, self.white_color, rect_form)
#                     elif numericValue == 2:
#                         rect_form = pygame.Rect(x * 50, y * 50, (x + 1) * 50, (y + 1) * 50)
#                         pygame.draw.rect(self.screen, self.white_color, rect_form)
#                     elif numericValue == 3:
#                         rect_form = pygame.Rect(x * 50, y * 50, (x + 1) * 50, (y + 1) * 50)
#                         pygame.draw.rect(self.screen, self.white_color, rect_form)
#
#
# xxxxxxxxxxxxxxx
# x.cx..........x
# xx..x..x..x...x
# x.x..x..xx.xx.x
# x..x..x.x..x..x
# x...x.x.x.x...x
# x.x...x.x...x.x
# x.xx.xxaxxxxx.x
# x.x..x.x....x.x
# x.x.x.....x.x.x
# x.x..x.x.x..x.x
# x.x.x..x..x.x.x
# x.xx..x.x..xx.x
# x....x........x
# xxxxxxxxxxxxxxx
#
# xxxxxxxxxxxxxxx
# .c............x
# x.xxxxxxxxx.x.x
# x.x.........x.x
# x..xxx.xxxx.x.x
# x.x........x..x
# x...xxxxx.x.x.x
# xxxx..ax.x....x
# x...x.x...x.x.x
# x.x....x.x..x.x
# x.x.x.x...xxx.x
# x.x..x........x
# x.xx.xxxxxxxx.x
# x.............x
# xxxxxxxxxxxxxxxoriginal
#
# c..............
# .xxxxxx.xxxx.x.
# .x.....x.....x.
# xx.xxx.x.xxx.x.
# ...x.x..x..x.x.
# .xx...x..x.x.x.
# .x.x.x..x..x.x.
# .x...xxaxx....x
# .x.x...x...x.x.
# .x.x.xx.xx.x.x.
# .x.x.......x.x.
# .x.xxxx.xxxx.x.
# .x.....x.......
# .x.xx.x..xxxxx.
# .......x.......
#
# c.x...x...x...x
# x...x...x...x..
# .x.x.xx..xx..x.
# .x...x.x.x.xx..
# ..x.x..x......x
# x.x.x.x.xxxxx..
# ..x.x.x.....ax.
# .x..x.x.xxxxx..
# ..xxx.x.x.....x
# x.....x.x.x.x..
# ..x.xxx.x.x..x.
# .x.......x..x..
# ..xx.xxx.xxx..x
# x...x...x...x..
# ..x...x...x...x
#
#
#
#
#
# https://www.developpez.net/forums/i1339621/autres-langages/python/programmation-multimedia-jeux/probleme-deplacement-personnage-pygame/
#
# arial_font = pygame.font.SysFont("arial", 30)
#         item_text = arial_font.render("item   /3", False, self.red)
#
#         self.screen.blit(item_text, [10,10])
#         pygame.display.flip()




# def mst(self):
#     # pygame.time.get_ticks()
#     rect_form = pygame.Rect(300, 600, 50, 50)
#     # pygame.draw.rect(self.screen, self.black_color, rect_form)
#     rect_form2 = pygame.Rect(350, 600, 50, 50)
#     pygame.display.flip()
#
#     while True:
#         # time.sleep(.010)
#         # self.screen.fill(self.black_color)
#         # self.screen.blit(self.taille_floor, (300, 550))
#         rect_form.x += 1
#         self.screen.blit(self.taille_mc, rect_form)
#         rect_form2.x -= 1
#         self.screen.blit(self.taille_floor, rect_form2)
#         pygame.display.flip()
#         if rect_form.x == 350:
#             return False
# """""""""""