from grille.grille import Grille
import random
import math


def prochaine_case(depart, destination):
    # Calcul des distances horizontales et verticales
    distance_horizontale = abs(depart[0] - destination[0])
    distance_verticale = abs(depart[1] - destination[1])

    # Calcul de la somme des distances pour avoir la probabilité
    total_distance = distance_horizontale + distance_verticale

    if total_distance == 0:
        return depart[0], depart[1]  # Cas où départ et destination sont identiques

    # Générer un nombre aléatoire et comparer à la proportion horizontale
    if random.random() < (distance_horizontale / total_distance):
        # Effectuer un mouvement horizontal
        if depart[0] > destination[0]:
            return depart[0] - 1, depart[1]
        elif depart[0] < destination[0]:
            return depart[0] + 1, depart[1]
    else:
        # Effectuer un mouvement vertical
        if depart[1] > destination[1]:
            return depart[0], depart[1] - 1
        elif depart[1] < destination[1]:
            return depart[0], depart[1] + 1

    return depart[0], depart[1]

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
            if self.moveClosest(g):
                break

            tentatives += 1

        return (0, 0)

    def moveRandom(self, g: Grille) -> bool:
        if random.choice([True, False]):
            new_x = self.x + random.choice([-1, 1])
            new_y = self.y
        else:  # Mouvement vertical
            new_x = self.x
            new_y = self.y + random.choice([-1, 1])

        if self.avancer(g, new_x, new_y):
            return True
        else:
            return False

    def moveClosest(self, g: Grille) -> bool:
        closestEnemy = self.getClosestEnemy(g)
        if closestEnemy != (0, 0):
            nextMove = prochaine_case((self.x, self.y), closestEnemy)
            if nextMove != (-1, -1):
                if self.avancer(g, nextMove[0], nextMove[1]):
                    return True
        return False


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
        return abs(self.x - enemy_pos[0]) + abs(self.y - enemy_pos[1]) < 2

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
