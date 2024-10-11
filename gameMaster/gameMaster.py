from agent.Agent import Agent
from grille.grille import Grille
import time

class GameMaster:
    def __init__(self,p1:Agent,p2:Agent):
        self.nbTours=0
        self.tabJoueur=[p1,p2]

    def AQuiDeJouer(self)->Agent:
        return self.tabJoueur[0]

    def tour(self,agent:Agent,g:Grille):
        self.nbTours+=1
        agent.jouer(g)
        self.tabJoueur.pop(0)
        self.tabJoueur.append(agent)
        time.sleep(0.5)







