from agent.Agent import Agent
from grille.grille import Grille
import time

class GameMaster:
    def __init__(self,listeAgents):
        self.nbTours=0
        self.tabJoueur=listeAgents

    def AQuiDeJouer(self)->Agent:
        return self.tabJoueur[0]

    def tour(self,agent:Agent,g:Grille):
        self.nbTours+=1
        agent.jouer(g)
        self.tabJoueur.pop(0)
        self.tabJoueur.append(agent)
        g.draw()
        time.sleep(0.5)







