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
            enemy=self.getClosestEnemy(g)
            #print("Je suis le joueur numero " + str(self.numEquipe) +" l'ennemi le + proche est " + str(enemy))
            nombre_aleatoire = random.randint(0, 1)
            if nombre_aleatoire == 0:
                x=random.randint(self.x-1, self.x+1)
                e=self.avancer(g,x,self.y)
                manger=self.manger(g)
                if manger:
                    return self.getClosestEnemy(g)
            elif nombre_aleatoire == 1:
                y=random.randint(self.y-1, self.y+1)
                e=self.avancer(g,self.x,y)
                manger = self.manger(g)
                if manger:
                    return self.getClosestEnemy(g)
            else:
                e=self.attendre()
        return (0,0)


    def avancer(self,g:Grille,x:int,y:int):
        g.remove_agent(self.x,self.y)
        e=g.place_agent(x,y,self.numEquipe)
        if not e:
            return False
        else:
            self.x = x
            self.y = y
            return True

    def manger(self,g:Grille):
        test=self.getClosestEnemy(g)
        if test==(0,1) or test==(1,0):
           return True
        else:
            return  False

    #def casseObstacle(self,g:Grille,x:int,y:int):

    def getClosestEnemy (self,g:Grille):
        resX=0
        resY=0
        min_dist=1111111
        for i in range(len (g.grid)):
            for j in range(len (g.grid[i])):
                if g.grid[i][j] > 0 and g.grid[i][j]!=self.numEquipe:
                    dist = abs(self.x - i) + abs(self.y - j)
                    if dist < min_dist:
                        min_dist = dist
                        resX = i
                        resY = j
        return  resX, resY

    def attendre(self):
        pass
