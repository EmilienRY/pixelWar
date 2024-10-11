import pygame
import sys
from grille.grille import Grille
from agent.Agent import Agent
from gameMaster.gameMaster import GameMaster

pygame.init()
WHITE = (255, 255, 255)

screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("PixelWar")

grille = Grille(10, 10, screen_width, screen_height,screen)
grille.place_agent(1, 1,1)
grille.place_agent(3, 5,2)
grille.place_obstacle(0, 0)
grille.place_obstacle(1, 0)
grille.place_obstacle(0, 1)
grille.place_obstacles(0, 2, 5)


a1=Agent(1,1,1)
a2=Agent(2,3,5)
master=GameMaster(a1,a2)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if(master.AQuiDeJouer().numPlayer==1):
        master.tour(a1,grille)
    else:
        master.tour(a2,grille)
    pygame.display.flip()

# Quitter Pygame proprement
pygame.quit()
sys.exit()
