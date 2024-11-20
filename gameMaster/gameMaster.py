from equipe.Equipe import Equipe
from grille.grille import Grille
from typing import List, Tuple, Optional
from Color.Color import Color

class GameMaster:
    posTeam = [
        lambda n, m: (0, 0, n // 3),  # Team 1
        lambda n, m: (n - m // 3, m - n // 3, m - 1),  # Team 2
        lambda n, m: (0, m - n // 3, m - 1),  # Team 3
        lambda n, m: (n - m // 3, 0, n // 3)  # Team 4
    ]

    def __init__(self, nb_teams: int, nbAgentsParEquipe: int, n: int, m: int, grid: Grille, coulTeam:[],nbObs):
        self.nb_obstacles = nbObs
        self.nb_tours = 0
        self.grid = grid
        self.coulTeam=coulTeam
        self.teams = self.initTeam(nb_teams, nbAgentsParEquipe, n, m)
        self.placeTeamEtObstacles()
        self.numTeamGagnante=0

    def initTeam(self, nb_teams: int, nbAgentsParEquipe: int, n: int, m: int) -> List[Equipe]:
        teams = []
        for i in range(nb_teams):
            start_x, start_y, limit = self.posTeam[i](n, m)
            team = Equipe(nbAgentsParEquipe, i + 1, self.coulTeam[i], start_x, start_y, limit)
            teams.append(team)
        return teams

    def placeTeamEtObstacles(self):
        for team in self.teams:
            for agent in team.listeEquipier:
                self.grid.place_agent(agent.x, agent.y, team.numEquipe)

        self.grid.place_obstacle(0, 0)
        self.grid.place_random_obstacles(self.nb_obstacles)
        self.grid.draw(self.coulTeam)

    def quiJoue(self) -> Equipe: #retourne team qui doit jouer
        return self.teams[0]

    def testFin(self) -> Tuple[bool, Optional[Equipe]]:

        teamEnJeu = [team for team in self.teams if team.listeEquipier]
        if len(teamEnJeu) == 1:
            return True, teamEnJeu[0]
        return False, None

    def tour(self) -> bool: # retourne false quand le jeu est fini

        game_over, winner = self.testFin()
        if game_over:
            self.numTeamGagnante=winner.numEquipe
            print(f"Jeu terminé! L'équipe {winner.numEquipe} a gagné!")
            return False

        self.nb_tours += 1
        teamQuiJoue = self.teams.pop(0)

        if teamQuiJoue.listeEquipier:
            joeur = teamQuiJoue.listeEquipier.pop(0)
            action = joeur.jouer(self.grid)

            if action != (0, 0):
                self.suprAgentManger(action)

            teamQuiJoue.listeEquipier.append(joeur)

        self.teams.append(teamQuiJoue)
        self.grid.draw(self.coulTeam)
        return True

    def suprAgentManger(self, position: Tuple[int, int]):
        x, y = position
        for team in self.teams:
            team.listeEquipier = [agent for agent in team.listeEquipier
                                  if not (agent.x == x and agent.y == y)]
        self.grid.grid[y][x] = 0

    def etatDujeu(self) -> dict:
        return {
            'nb_tours': self.nb_tours,
            'statu equipe': [{
                'num equipe': team.numEquipe,
                'agents restant': len(team.listeEquipier),
                'team':team
            } for team in self.teams]
        }