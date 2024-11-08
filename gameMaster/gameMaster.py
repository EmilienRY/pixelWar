from agent.Agent import Agent
from equipe.Equipe import Equipe
from grille.grille import Grille
import time

listeColor=[(0, 0, 255),(255, 0, 0),(255, 255, 0),(0, 255, 0)]

class GameMaster:

    def __init__(self, nbTeam, nbAgentsParTeam, n, m,g:Grille):
        tabEquipes = []
        for i in range(nbTeam):
            if i == 0:
                equipe1 = Equipe(nbAgentsParTeam, i + 1, listeColor[i], 0, 0, n // 3)
                tabEquipes.append(equipe1)
            elif i==1:
                equipe2 = Equipe(nbAgentsParTeam, i + 1, listeColor[i], n - m // 3, 0, n // 3)
                tabEquipes.append(equipe2)
            elif i==2:
                equipe3 = Equipe(nbAgentsParTeam, i + 1, listeColor[i], 0, m - n // 3, m - 1)
                tabEquipes.append(equipe3)
            elif i==3:
                equipe4 = Equipe(nbAgentsParTeam, i + 1, listeColor[i], n - m // 3, m - n // 3, m - 1)
                tabEquipes.append(equipe4)

        self.nbTours=0
        self.tabEquipes=tabEquipes

        for i in range(nbTeam):
            for j in range(nbAgentsParTeam):
                g.place_agent(self.tabEquipes[i].listeEquipier[j].x, self.tabEquipes[i].listeEquipier[j].y, self.tabEquipes[i].numEquipe)

        self.grille=g
        g.draw()
        self.grille.place_obstacle(0, 0)
        self.grille.place_random_obstacles(20)


    def AQuiDeJouer(self) -> Equipe:
        return self.tabEquipes[0]

    def tour(self,g:Grille):
        self.nbTours += 1
        equipe=self.tabEquipes.pop(0)
        player=equipe.listeEquipier.pop(0)
        player.jouer(g)
        equipe.listeEquipier.append(player)
        self.tabEquipes.append(equipe)
        g.draw()







