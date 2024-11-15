import pygame
import random
import math
from Color.Color import Color


class Grille:

    def __init__(self, n:int, m:int, screen_width:int, screen_height:int,screen):
        self.n = n  # Nombre de lignes
        self.m = m  # Nombre de colonnes
        self.screen=screen
        # on calcule la taille des cases en fonction du nombre de cases
        self.cell_width = screen_width // m
        self.cell_height = screen_height // n
        self.grid = [[0 for _ in range(m)] for _ in range(n)]  # Matrice n*m remplie de 0

    def draw(self,coulTeam):
        """Dessiner la grille sur l'écran"""
        self.screen.fill(Color.WHITE.value)
        for x in range(self.m):
            for y in range(self.n):
                rect = pygame.Rect(x * self.cell_width, y * self.cell_height, self.cell_width, self.cell_height)
                pygame.draw.rect(self.screen, Color.BLACK.value, rect, 1)  # Dessiner le contour des cases
                if self.grid[y][x] == -1:
                    pygame.draw.rect(self.screen, Color.BLACK.value, rect)
                if self.grid[y][x] == 1:
                    pygame.draw.rect(self.screen, coulTeam[0].value, rect)
                if self.grid[y][x] == 2:
                    pygame.draw.rect(self.screen, coulTeam[1].value, rect)
                if self.grid[y][x] == 3:
                    pygame.draw.rect(self.screen, coulTeam[2].value, rect)
                if self.grid[y][x] == 4:
                    pygame.draw.rect(self.screen, coulTeam[3].value, rect)


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
            x = random.randint(0, self.n - 1)
            y = random.randint(0, self.m - 1)

            if self.grid[x][y] == 0:
                self.grid[x][y] = -1
                obstacles_placed += 1

                if obstacles_placed < nbObstacles and random.random() < 0.5:
                    new_y: int
                    new_x:int
                    new_x, new_y = self._place_adjacent_obstacle(x, y)
                    obstacles_placed += 1

                    if obstacles_placed < nbObstacles and random.random() < 0.3:
                        chosen_obstacle:bool = random.random() < 0.5
                        self._place_adjacent_obstacle(x if chosen_obstacle else new_x, y if chosen_obstacle else new_y)
                        obstacles_placed += 1

    def _place_adjacent_obstacle(self, x, y):
        """Attempt to place one obstacle randomly adjacent to the given position (x, y)"""
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
                      (-1, -1), (-1, 1), (1, -1), (1, 1)]
        random.shuffle(directions)

        dx, dy = directions[0]
        new_x, new_y = x + dx, y + dy

        if 0 <= new_x < self.n and 0 <= new_y < self.m and self.grid[new_x][new_y] == 0:
            self.grid[new_x][new_y] = -1  # Place the obstacle at the valid adjacent position
        return new_x,new_y

    def place_agent(self, x:int, y:int, team:int):
        """Placer un objet à la position (x, y) dans la grille"""
        if 0 <= x < self.m and 0 <= y < self.n and self.grid[y][x] ==0:
            self.grid[y][x] = team
            return True
        else :
            return False

    def obstacle_plus_proche(self, x: int, y: int):
        obstacles_proches = []
        distance_min = 1000000

        for i in range(self.n):
            for j in range(self.m):
                if self.grid[i][j] == -1:  # Trouver un obstacle
                    distance = math.sqrt((i - x) ** 2 + (j - y) ** 2)
                    if distance < distance_min:
                        distance_min = distance
                        obstacles_proches = [(i, j)]
                    elif distance == distance_min:
                        obstacles_proches.append((i, j))

        return obstacles_proches

    def remove_obstacle(self, x: int, y: int):
        """Retirer un obstacle de la position (x, y) dans la grille"""
        if 0 <= x < self.m and 0 <= y < self.n and self.grid[y][x] == -1:
            self.grid[y][x] = 0

    def afficher_grille(self):
        for ligne in self.grid:
            print(ligne)



    def remove_agent(self, x:int, y:int):
            """Retirer un objet de la position (x, y) dans la grille"""
            if 0 <= x < self.m and 0 <= y < self.n:
                self.grid[y][x] = 0







