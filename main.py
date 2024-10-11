import pygame
import sys
from grille.grille import Grille
from agent.AgentTest import AgentTest
from gameMaster.gameMaster import GameMaster
from gameMaster.menu import Menu  # Import the new Menu class

pygame.init()

WHITE = (255, 255, 255)

screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("PixelWar")

# Run the Menu and get game settings
menu = Menu(screen)
grid_width, grid_height, num_players = menu.run_menu()

# Initialize the grid and game master based on the settings
grille = Grille(grid_width, grid_height, screen_width, screen_height, screen)

# Set up players
agents = []
for i in range(1, num_players + 1):
    # You can place the players differently; for now, we'll put them in different coordinates
    agents.append(AgentTest(i, i * 2, i * 2))  # Example placement

master = GameMaster(*agents)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    current_player = master.AQuiDeJouer()

    if current_player.numPlayer == 1:
        master.tour(agents[0], grille)
    elif current_player.numPlayer == 2 and num_players > 1:
        master.tour(agents[1], grille)

    pygame.display.flip()

# Quit Pygame properly
pygame.quit()
sys.exit()
