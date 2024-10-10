import pygame
import sys
from grille.grille import Grille
from agent.AgentTest import AgentTest
from gameMaster.gameMaster import GameMaster

pygame.init()
WHITE = (255, 255, 255)

screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("PixelWar")

grille = Grille(10, 10, screen_width, screen_height,screen)
grille.place_agent(1, 1,1)
grille.place_agent(3, 5,2)
a1=AgentTest(1,1,1)
a2=AgentTest(2,3,5)
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
