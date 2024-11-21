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

        self.cptOstaclesdetruit=0
        self.mouvAleatoir=0
        self.mouvPasAleatoir=0
        self.nbAgentsMange=0
        self.AgroCasseObs=0
        self.defAMange=0
        self.distanceParcouru=0
        self.defAFui=0

        self.comportement = random.choices(
            ["agressif", "defensif", "fou"],
            weights=[0.4, 0.4, 0.2],
            k=1
        )[0]





    def vaSeFaireManger(self, new_x,new_y,enemy_pos):

        distance = abs(new_x - enemy_pos[0]) + abs(new_y - enemy_pos[1])

        if distance <= 2:
            return True
        else:
            return False

    def jump(self,g: Grille,enemy_pos ):
        newX=int((self.x+enemy_pos[0])/2)
        newY=int((self.y+enemy_pos[1])/2)
        self.avancer(g, newX, newY)


    def jouer(self, g: Grille):
        if self.comportement == "fou":
            action=self.action_fou(g)
            if action[0]:
                return action[1] if action[1] != None else (0,0)
        elif self.comportement == "agressif":
            action=self.action_agressive(g)
            if action[0]:
                return action[1] if action[1] != None else (0,0)
        elif self.comportement == "defensif":
            action=self.action_defensive(g)
            if action[0]:
                return action[1] if action[1] != None else (0,0)

        self.moveRandom(g)
        return (0, 0)

    def action_fou(self,g:Grille):
        enemy_pos = self.getClosestEnemy(g)
        if enemy_pos != (0, 0) and self.peut_manger(g, enemy_pos):
            if abs(self.x - enemy_pos[0]) == 2 or abs(self.y - enemy_pos[1]) == 2:
                self.jump(g, enemy_pos)
            self.nbAgentsMange+=1
            return (True,enemy_pos)

        obstacle = self.verifier_obstacle_adjacent(g)
        if obstacle[0]:
            x, y = obstacle[1]
            self.casseObstacle(g, x, y)
            self.AgroCasseObs+=1
            return (True,None)

        if self.moveRandom(g):
            return (True,None)

    def action_agressive(self, g: Grille):
        enemy_pos = self.getClosestEnemy(g)
        if enemy_pos != (0, 0) and self.peut_manger(g, enemy_pos):
            if abs(self.x - enemy_pos[0]) == 2 or abs(self.y - enemy_pos[1]) == 2:
                self.jump(g, enemy_pos)
            self.nbAgentsMange+=1
            return (True,enemy_pos)

        if self.moveClosest(g):
            return (True,None)

        obstacle = self.verifier_obstacle_adjacent(g)
        if obstacle[0]:
            x, y = obstacle[1]
            self.casseObstacle(g, x, y)
            self.AgroCasseObs+=1
            return (True,None)

        return (False,None)


    def action_defensive(self, g: Grille):
        enemy_pos = self.getClosestEnemy(g)
        if enemy_pos != (0, 0) and self.vaSeFaireManger(self.x, self.y, enemy_pos):
            if self.moveRandom(g):
                self.defAFui+=1
                return (True,None)

        obstacle = self.verifier_obstacle_adjacent(g)
        if obstacle[0]:
            x, y = obstacle[1]
            self.casseObstacle(g, x, y)
            return (True,None)

        enemy_pos = self.getClosestEnemy(g)
        if enemy_pos != (0, 0) and self.peut_manger(g, enemy_pos):
            if abs(self.x - enemy_pos[0]) == 2 or abs(self.y - enemy_pos[1]) == 2:
                self.jump(g, enemy_pos)
            self.defAMange+=1
            self.nbAgentsMange+=1
            return (True,enemy_pos)

        if self.moveRandom(g):
            return (True,None)

        return (False,None)

    def moveRandom(self, g: Grille) -> bool:
        self.mouvAleatoir += 1
        for _ in range(self.max_tentatives):
            if random.choice([True, False]):
                new_x = self.x + random.choice([-1, 1])
                new_y = self.y
            else:
                new_x = self.x
                new_y = self.y + random.choice([-1, 1])

            if self.avancer(g, new_x, new_y):
                return True
        return False


    def moveClosest(self, g: Grille) -> bool:
        self.mouvPasAleatoir+=1
        closestEnemy = self.getClosestEnemy(g)
        if closestEnemy != (0, 0):
            nextMove = prochaine_case((self.x, self.y), closestEnemy)
            if not self.vaSeFaireManger(nextMove[0], nextMove[1], closestEnemy):
                if self.avancer(g, nextMove[0], nextMove[1]):
                    return True

        return False


    def verifier_obstacle_adjacent(self, g: Grille, use_strategy=True):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dx, dy in directions:
            new_x = self.x + dx
            new_y = self.y + dy
            if (0 <= new_x < g.m and 0 <= new_y < g.n and g.grid[new_y][new_x] == -1):
                if use_strategy:
                    closestEnemy = self.getClosestEnemy(g)
                    if closestEnemy != (0, 0):
                        if abs(new_x - closestEnemy[0]) + abs(new_y - closestEnemy[1]) > 2:
                            return (True, (new_x, new_y))
                else:
                    return (True, (new_x, new_y))
        return (False, (None, None))


    def peut_manger(self, grille: Grille, enemy_pos: tuple) -> bool:
        dx = abs(self.x - enemy_pos[0])
        dy = abs(self.y - enemy_pos[1])

        if not ((dx <= 2 and dy == 0) or (dy <= 2 and dx == 0)):
            return False

        mid_x = int((self.x + enemy_pos[0]) / 2)
        mid_y = int((self.y + enemy_pos[1]) / 2)

        if grille.grid[mid_y][mid_x] == -1:
            return False

        return True

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
        self.distanceParcouru+=1
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
        self.cptOstaclesdetruit+=1
        if 0 <= x < g.m and 0 <= y < g.n and g.grid[y][x] == -1:
            g.remove_obstacle(x, y)
