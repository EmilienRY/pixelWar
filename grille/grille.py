import pygame
import random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)

class Grille:

    def __init__(self, n:int, m:int, screen_width:int, screen_height:int,screen):
        self.n = n  # Nombre de lignes
        self.m = m  # Nombre de colonnes
        self.screen=screen
        # on calcule la taille des cases en fonction du nombre de cases
        self.cell_width = screen_width // m
        self.cell_height = screen_height // n
        self.grid = [[0 for _ in range(m)] for _ in range(n)]  # Matrice n*m remplie de 0


    def draw(self):
        """Dessiner la grille sur l'écran"""
        self.screen.fill(WHITE)
        for x in range(self.m):
            for y in range(self.n):
                rect = pygame.Rect(x * self.cell_width, y * self.cell_height, self.cell_width, self.cell_height)
                pygame.draw.rect(self.screen, BLACK, rect, 1)  # Dessiner le contour des cases
                if self.grid[y][x] == -1:
                    pygame.draw.rect(self.screen, BLACK, rect)
                if self.grid[y][x] == 1:
                    pygame.draw.rect(self.screen, YELLOW, rect)
                if self.grid[y][x] == 2:
                    pygame.draw.rect(self.screen, GREEN, rect)

    def place_obstacle(self, x:int, y:int):
        """Placer un objet à la position (x, y) dans la grille"""
        if 0 <= x < self.m and 0 <= y < self.n:
                self.grid[y][x] = -1

    def place_obstacles(self, x: int, x2: int, y: int):
        """Placer des objets à la position (x:x2, y) dans la grille"""
        if 0 <= x < self.m and 0 <= y < self.n:
            for i in range(x,x2+1,1):
             self.grid[y][i] = -1

    def place_random_obstacles(self, nbObstacles: int):
        """Placer des obstacles aléatoirement dans la grille"""
        obstacles_placed = 0
        while obstacles_placed < nbObstacles:
            # Randomly select a position in the grid
            x = random.randint(0, self.n - 1)
            y = random.randint(0, self.m - 1)

            # Only place an obstacle if the position is empty
            if self.grid[x][y] == 0:
                self.grid[x][y] = -1
                obstacles_placed += 1

                # Now, decide if we place a connected obstacle
                if obstacles_placed < nbObstacles and random.random() < 0.5:
                    # Try to place a second obstacle adjacent to the first one
                    new_y: int
                    new_x:int
                    new_x, new_y = self._place_adjacent_obstacle(x, y)
                    obstacles_placed += 1

                    # Try to place a third obstacle with a reduced probability
                    if obstacles_placed < nbObstacles and random.random() < 0.3:
                        # Try to place a third obstacle adjacent to the second one
                        chosen_obstacle:bool = random.random() < 0.5
                        self._place_adjacent_obstacle(x if chosen_obstacle else new_x, y if chosen_obstacle else new_y)
                        obstacles_placed += 1



    def _place_adjacent_obstacle(self, x, y):
        """Attempt to place one obstacle randomly adjacent to the given position (x, y)"""
        # Possible directions to move: (dx, dy) pairs for 8 directions (up, down, left, right, diagonals)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
                      (-1, -1), (-1, 1), (1, -1), (1, 1)]
        random.shuffle(directions)  # Shuffle to randomize the directions

        # Pick the first direction after shuffle and attempt to place the obstacle
        dx, dy = directions[0]
        new_x, new_y = x + dx, y + dy

        # Ensure the new position is valid and empty
        if 0 <= new_x < self.n and 0 <= new_y < self.m and self.grid[new_x][new_y] == 0:
            self.grid[new_x][new_y] = -1  # Place the obstacle at the valid adjacent position
        return new_x,new_y



    def place_agent(self, x:int, y:int, team:int):
        """Placer un objet à la position (x, y) dans la grille"""
        if 0 <= x < self.m and 0 <= y < self.n:
            if self.grid[y][x]>=0:
                self.grid[y][x] = team

    def remove_agent(self, x:int, y:int):
            """Retirer un objet de la position (x, y) dans la grille"""
            if 0 <= x < self.m and 0 <= y < self.n:
                self.grid[y][x] = 0







