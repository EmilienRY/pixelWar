from grille.grille import Grille
import random

class Agent:
    def __init__(self,num,x,y):
        self.numPlayer=num
        self.x=x
        self.y=y


    def jouer(self,g:Grille):
        nombre_aleatoire = random.randint(0, 2)
        if( nombre_aleatoire == 0):
            x=random.randint(self.x-1, self.x+1)
            self.avancer(g,x,self.y)
        elif(nombre_aleatoire == 1):
            y=random.randint(self.y, self.y+1)
            self.avancer(g,self.x,y)
        else:
            self.attendre()


    def avancer(self,g:Grille,x:int,y:int):
        g.remove_agent(self.x,self.y)
        g.place_agent(x,y,self.numPlayer)
        self.x = x
        self.y = y

    #def manger(self,g:Grille,x:int,y:int):

    #def casseObstacle(self,g:Grille,x:int,y:int):


    def attendre(self):
        pass














