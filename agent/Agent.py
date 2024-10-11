
from grille.grille import Grille


class Agent:
    def __init__(self,num,x,y):
        self.numPlayer=num
        self.x=x
        self.y=y

    def jouer(self,g:Grille):
        g.remove_agent(self.x,self.y)
        self.x+=1
        g.place_agent(self.x,self.y,self.numPlayer)
        g.draw()

    def avancer(self,g:Grille,x:int,y:int):
        g.remove_agent(self.x,self.y)
        g.place_agent(self.x,self.y,self.numPlayer)
        self.x = x
        self.y = y













