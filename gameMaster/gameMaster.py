from agent.AgentTest import AgentTest
from grille.grille import Grille
import time

class GameMaster:
    def __init__(self,p1:AgentTest,p2:AgentTest):
        self.nbTours=0
        self.tabJoueur=[p1,p2]

    def AQuiDeJouer(self)->AgentTest:
        return self.tabJoueur[0]

    def tour(self,agent:AgentTest,g:Grille):
        self.nbTours+=1
        agent.jouer(g)
        self.tabJoueur.pop(0)
        self.tabJoueur.append(agent)
        time.sleep(0.5)







