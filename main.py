import time
import pygame
import sys
from grille.grille import Grille
from gameMaster.gameMaster import GameMaster
from Menu.menu import Menu

def main():
    pygame.init()


    game_width, game_height = 1000, 1000
    sidebar_width = 800  # zone des infos
    screen_width = game_width + sidebar_width
    screen_height = game_height

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("PixelWar")
    acceuil=Menu(screen)
    acceuil.run_menu()
    nbTeam=acceuil.num_team
    nbObs=acceuil.nb_obs
    nbAgentPerTeam=acceuil.num_agent
    nbLigne=acceuil.grid_height
    nbColone=acceuil.grid_width
    ColorTeam1=acceuil.color[acceuil.i]
    ColorTeam2=acceuil.color[acceuil.j]
    ColorTeam3=acceuil.color[acceuil.k]
    ColorTeam4=acceuil.color[acceuil.l]
    colorTeams= [ColorTeam1,ColorTeam2,ColorTeam3,ColorTeam4]
    grille = Grille(nbLigne, nbColone, game_width, game_height, screen)
    try:
        master = GameMaster(nbTeam, nbAgentPerTeam, nbLigne, nbColone, grille, colorTeams,nbObs)
    except ValueError as e:
        print(f"Erreur lors de l'initialisation du jeu : {e}")
        return

    policeTitre = pygame.font.Font(None, 36)
    policeInfo = pygame.font.Font(None, 24)
    clock = pygame.time.Clock()
    nbToursSecondes = acceuil.nbToursSec # nb de tour par secondes

    def drawBarreCote(etatJeu):
        sidebar_rect = pygame.Rect(game_width, 0, sidebar_width, screen_height)
        pygame.draw.rect(screen, (240, 240, 240), sidebar_rect)
        pygame.draw.line(screen, (200, 200, 200), (game_width, 0), (game_width, screen_height), 2)

        title = policeTitre.render("Informations", True, (0, 0, 0))
        screen.blit(title, (game_width + 10, 10))

        y_offset = 60
        tour_text = policeInfo.render(f"Tour: {etatJeu['nb_tours']}", True, (0, 0, 0))
        screen.blit(tour_text, (game_width + 10, y_offset))

        y_offset += 40
        pygame.draw.line(screen, (200, 200, 200),
                         (game_width + 10, y_offset),
                         (screen_width - 10, y_offset), 1)

        y_offset += 20
        teams_title = policeTitre.render("Équipes", True, (0, 0, 0))
        screen.blit(teams_title, (game_width + 10, y_offset))

        y_offset += 40
        sorted_teams=sorted(etatJeu['statu equipe'], key=lambda x: x['num equipe'])
        for team in sorted_teams:
            team_color = colorTeams[team['num equipe'] - 1]
            pygame.draw.rect(screen, team_color.value,
                             (game_width + 10, y_offset, 20, 20))

            team_text = policeInfo.render(
                f"Équipe {team['num equipe']}: {team['agents restant']} agents",
                True, (0, 0, 0)
            )
            screen.blit(team_text, (game_width + 40, y_offset))
            y_offset += 30

        y_offset += 20
        pygame.draw.line(screen, (200, 200, 200),
                         (game_width + 10, y_offset),
                         (screen_width - 10, y_offset), 1)

        stats_title = policeTitre.render("Statistiques", True, (0, 0, 0))
        screen.blit(stats_title, (game_width + 10, y_offset + 20))

        y_offset += 60


        for team_info in sorted_teams:
            team = team_info['team']

            obstacles_detruits = sum(agent.cptOstaclesdetruit for agent in team.listeEquipier)
            mouvements_aleatoires = sum(agent.mouvAleatoir for agent in team.listeEquipier)
            mouvements_non_aleatoires = sum(agent.mouvPasAleatoir for agent in team.listeEquipier)
            nbAgentsMange = sum(agent.nbAgentsMange for agent in team.listeEquipier)
            AgroCasseObs = sum(agent.AgroCasseObs for agent in team.listeEquipier)
            defAMange = sum(agent.defAMange for agent in team.listeEquipier)
            distanceParcouru = sum(agent.distanceParcouru for agent in team.listeEquipier)
            defAFui = sum(agent.defAFui for agent in team.listeEquipier)


            stats_team_textTyp = policeInfo.render(
                f"Équipe {team.numEquipe} - agressifs: {team.nbAgro}, défensifs: {team.nbDef}",
                True, (0, 0, 0)
            )
            stats_team_textTyp2 = policeInfo.render(
                f"Équipe {team.numEquipe} -fous: {team.nbFou}, support: {team.nbSupport} ",
                True, (0, 0, 0)
            )

            statsObsDetr = policeInfo.render(
                f"Équipe {team.numEquipe} - Obstacles détruits: {obstacles_detruits}",
                True, (0, 0, 0)
            )
            statsMvtAlea = policeInfo.render(
                f"Équipe {team.numEquipe} - Mvt aléatoires: {mouvements_aleatoires}",
                True, (0, 0, 0)
            )
            statsMvtNonAlea = policeInfo.render(
                f"Équipe {team.numEquipe} - Mvt non-aléatoires: {mouvements_non_aleatoires}",
                True, (0, 0, 0)
            )

            statAgenMange = policeInfo.render(
                f"Équipe {team.numEquipe} - Agents mangé {nbAgentsMange} ",
                True, (0, 0, 0)
            )

            statsAgroCasse = policeInfo.render(
                f"Équipe {team.numEquipe} - Obstacles détruits par agressif: {AgroCasseObs}",
                True, (0, 0, 0)
            )
            statDefMange = policeInfo.render(
                f"Équipe {team.numEquipe} - agents mangé par défensif: {defAMange}",
                True, (0, 0, 0)
            )
            statDistance = policeInfo.render(
                f"Équipe {team.numEquipe} - distance parcourue: {distanceParcouru}",
                True, (0, 0, 0)
            )
            statDefFui = policeInfo.render(
                f"Équipe {team.numEquipe} - defensif a fui: {defAFui}",
                True, (0, 0, 0)
            )

            x_colonne1 = game_width + 10
            x_colonne2 = game_width + 400
            screen.blit(stats_team_textTyp, (x_colonne1, y_offset))
            y_offset += 25
            screen.blit(stats_team_textTyp2, (x_colonne1, y_offset))
            y_offset += 25
            screen.blit(statsObsDetr, (x_colonne1, y_offset))
            y_offset += 25
            screen.blit(statsMvtAlea, (x_colonne1 , y_offset))
            y_offset += 25
            screen.blit(statsMvtNonAlea, (x_colonne1, y_offset))
            y_offset-=75
            screen.blit(statAgenMange, (x_colonne2, y_offset))
            y_offset += 25
            screen.blit(statsAgroCasse, (x_colonne2, y_offset))
            y_offset += 25
            screen.blit(statDefMange, (x_colonne2, y_offset))
            y_offset += 25
            screen.blit(statDistance, (x_colonne2, y_offset))
            y_offset += 25
            screen.blit(statDefFui, (x_colonne2, y_offset))

            y_offset += 35

    running = True
    paused = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = not paused
                elif event.key == pygame.K_ESCAPE:
                    running = False

        if not paused:
            screen.fill((255, 255, 255))

            if not master.tour():
                game_state = master.etatDujeu()
                team_color = colorTeams[master.numTeamGagnante-1]
                text = policeTitre.render(f"Jeu terminé ! La team {master.numTeamGagnante} a gagné au tour : {game_state['nb_tours']}", True, team_color.value)
                text_rect = text.get_rect(center=(game_width // 2, game_height // 2))
                screen.blit(text, text_rect)
                pygame.display.flip()
                time.sleep(3)
                running = False
                continue

            game_state = master.etatDujeu()
            drawBarreCote(game_state)

            if paused:
                pause_text = policeTitre.render("PAUSE", True, (255, 0, 0))
                text_rect = pause_text.get_rect(center=(game_width // 2, game_height // 2))
                screen.blit(pause_text, text_rect)

            pygame.display.flip()
            clock.tick(nbToursSecondes)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()