from grille.grille import Grille
import random
import math

class Agent:
    def __init__(self, numJoueur: int, numEquipe: int, x: int, y: int):

        self.numEquipe = numEquipe
        self.numPlayer = numJoueur
        self.x = x
        self.y = y
        self.max_tentatives = 10

    def jouer(self, g: Grille):

        enemy_pos = self.getClosestEnemy(g)
        if enemy_pos != (0, 0) and self.peut_manger(g, enemy_pos):
            return enemy_pos

        if self.verifier_obstacle_adjacent(g):
            return (0, 0)

        tentatives = 0
        while tentatives < self.max_tentatives:
            if random.choice([True, False]):
                new_x = self.x + random.choice([-1, 1])
                new_y = self.y
            else:  # Mouvement vertical
                new_x = self.x
                new_y = self.y + random.choice([-1, 1])

            if self.avancer(g, new_x, new_y):
                break

            tentatives += 1

        return (0, 0)

    def verifier_obstacle_adjacent(self, g: Grille) -> bool: # verif si obstacle a coté

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for dx, dy in directions:
            new_x = self.x + dx
            new_y = self.y + dy

            if (0 <= new_x < g.m and 0 <= new_y < g.n and
                    g.grid[new_y][new_x] == -1):
                self.casseObstacle(g, new_x, new_y)
                return True

        return False

    def peut_manger(self, g: Grille, enemy_pos: tuple) -> bool:

        enemy_x, enemy_y = enemy_pos

        if self.x == enemy_x:
            if abs(self.y - enemy_y) == 2:
                middle_y = (self.y + enemy_y) // 2
                return (g.grid[middle_y][self.x] == 0 and
                        g.grid[enemy_y][enemy_x] > 0 and
                        g.grid[enemy_y][enemy_x] != self.numEquipe)
        elif self.y == enemy_y:
            if abs(self.x - enemy_x) == 2:
                middle_x = (self.x + enemy_x) // 2
                return (g.grid[self.y][middle_x] == 0 and
                        g.grid[enemy_y][enemy_x] > 0 and
                        g.grid[enemy_y][enemy_x] != self.numEquipe)

        return False

    def avancer(self, g: Grille, x: int, y: int) -> bool:

        if not (0 <= x < g.m and 0 <= y < g.n):
            return False

        if g.grid[y][x] != 0:
            return False

        g.remove_agent(self.x, self.y)
        e = g.place_agent(x, y, self.numEquipe)
        if e:
            self.x = x
            self.y = y
        return e

    def getClosestEnemy(self, g: Grille) -> tuple:

        min_dist = float('inf')
        res_x, res_y = 0, 0
        found_enemy = False

        for i in range(g.n):
            for j in range(g.m):
                if g.grid[i][j] > 0 and g.grid[i][j] != self.numEquipe:
                    # Distance de Manhattan (pas de diagonale)
                    dist = abs(self.x - j) + abs(self.y - i)
                    if dist < min_dist:
                        min_dist = dist
                        res_x = j
                        res_y = i
                        found_enemy = True

        return (res_x, res_y) if found_enemy else (0, 0)

    def casseObstacle(self, g: Grille, x: int, y: int):
         if 0 <= x < g.m and 0 <= y < g.n and g.grid[y][x] == -1:
            g.remove_obstacle(x, y)
