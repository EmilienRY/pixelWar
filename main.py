import pygame
import sys
from grille.grille import Grille

pygame.init()

screen_width, screen_height = 1000, 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("PixelWar")

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Taille des cellules de la grille
cell_size = 50

g:Grille

g.__init__(10,10)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    for x in range(0, screen_width, cell_size):
        for y in range(0, screen_height, cell_size):
            rect = pygame.Rect(x, y, cell_size, cell_size)
            pygame.draw.rect(screen, BLACK, rect, 1)

    pygame.display.flip()

pygame.quit()
sys.exit()
