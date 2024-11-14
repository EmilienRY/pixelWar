from agent.Agent import (Agent)

class Equipe:

    def __init__(self,nbJoueursParTeam,numEquipe,color,xStart,yStart,yMax):

        self.nbDeJoueurs=nbJoueursParTeam

        self.numEquipe=numEquipe

        self.color=color

        listeEquipier=[]

        x=xStart
        y=yStart

        for i in range(nbJoueursParTeam):
            if y+1 < yMax:
                y+=1
            else:
                y=yStart
                x+=1

            a=Agent(i,numEquipe,x,y)
            listeEquipier.append(a)
        self.listeEquipier=listeEquipier
