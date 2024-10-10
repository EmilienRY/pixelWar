import pygame
import sys
from grille.grille import Grille

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Fenêtre avec Grille et Objets")

cell_size = 10
grille = Grille(10, 10, screen_width, screen_height,screen)
grille.place_agent(1, 1,1)
grille.place_agent(3, 5,2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    grille.draw()

    pygame.display.flip()

# Quitter Pygame proprement
pygame.quit()
sys.exit()
