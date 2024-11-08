from grille.grille import Grille
import random

class Agent:

    def __init__(self,numJoueur,numEquipe,x,y):
        self.numEquipe=numEquipe
        self.numPlayer=numJoueur
        self.x = x
        self.y = y

    def jouer(self,g:Grille):
        e=False
        while not e:
            nombre_aleatoire = random.randint(0, 1)
            if nombre_aleatoire == 0:
                x=random.randint(self.x-1, self.x+1)
                e=self.avancer(g,x,self.y)
            elif nombre_aleatoire == 1:
                y=random.randint(self.y-1, self.y+1)
                e=self.avancer(g,self.x,y)
            else:
                e=self.attendre()


    def avancer(self,g:Grille,x:int,y:int):
        g.remove_agent(self.x,self.y)
        e=g.place_agent(x,y,self.numEquipe)
        if not e:
            return False
        else:
            self.x = x
            self.y = y
            return True

    #def manger(self,g:Grille,x:int,y:int):

    #def casseObstacle(self,g:Grille,x:int,y:int):


    def attendre(self):
        pass
