
from grille.grille import Grille


class AgentTest:
    def __init__(self,num,x,y):
        self.numPlayer=num
        self.x=x
        self.y=y

    def jouer(self,g:Grille):
        g.remove_agent(self.x,self.y)
        self.x+=1
        g.place_agent(self.x,self.y,self.numPlayer)
        g.draw()








