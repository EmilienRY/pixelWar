import time
import pygame
import sys
from grille.grille import Grille
from gameMaster.gameMaster import GameMaster
from Menu.menu import Menu

def main():
    pygame.init()


    game_width, game_height = 600, 600  # Zone de jeu carrée
    sidebar_width = 200  # zone des infos
    screen_width = game_width + sidebar_width
    screen_height = game_height

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("PixelWar")
    acceuil=Menu(screen)
    acceuil.run_menu()
    nbTeam=acceuil.num_team
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
        master = GameMaster(nbTeam, nbAgentPerTeam, nbLigne, nbColone, grille, colorTeams)
    except ValueError as e:
        print(f"Erreur lors de l'initialisation du jeu : {e}")
        return

    policeTitre = pygame.font.Font(None, 36)
    policeInfo = pygame.font.Font(None, 24)
    clock = pygame.time.Clock()
    nbToursSecondes = 5 # nb de tour par secondes

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
        for team in etatJeu['statu equipe']:
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
        stats_placeholder = policeInfo.render("(Statistiques à venir)", True, (100, 100, 100))
        screen.blit(stats_placeholder, (game_width + 10, y_offset))

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
                text = policeTitre.render(f"Jeu terminé ! Tour final : {game_state['nb_tours']}", True, (255, 0, 0))
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