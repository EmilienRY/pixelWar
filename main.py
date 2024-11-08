import pygame
import sys
from grille.grille import Grille
from gameMaster.gameMaster import GameMaster

pygame.init()
WHITE = (255, 255, 255)

screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("PixelWar")

grille = Grille(20,20,screen_width, screen_height,screen)

master = GameMaster(4, 25, 10, 10, grille)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    master.tour(grille)
    pygame.display.flip()

# Quitter Pygame proprement
pygame.quit()
sys.exit()
