import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

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
                if self.grid[y][x] == 1:
                    pygame.draw.rect(self.screen, BLUE, rect)
                if self.grid[y][x] == 2:
                    pygame.draw.rect(self.screen, RED, rect)

    def place_agent(self, x:int, y:int, team:int):
        """Placer un objet à la position (x, y) dans la grille"""
        if 0 <= x < self.m and 0 <= y < self.n:
            if self.grid[y][x]>=0:
                self.grid[y][x] = team

    def remove_agent(self, x:int, y:int):
            """Retirer un objet de la position (x, y) dans la grille"""
            if 0 <= x < self.m and 0 <= y < self.n:
                self.grid[y][x] = 0







