import pygame
import sys
import time
from Color.Color import Color

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)
        self.grid_width = 10
        self.grid_height = 10
        self.num_team = 2  # Default number of team
        self.num_agent = 2
        self.nb_obs=20
        self.color=[Color.BLUE,Color.RED,Color.YELLOW,Color.GREEN,Color.ORANGE,Color.CYAN,Color.MAGENTA,Color.GRAY,Color.PURPLE,Color.PINK]
        self.i=0
        self.j=1
        self.k=2
        self.l=3
        self.alert=False

    def draw_text(self, text, x, y, color):
        text_surface = self.font.render(text, True, color)
        self.screen.blit(text_surface, (x, y))

    def draw_arrow(self, x, y, direction):
        """Draws a left or right arrow."""
        if direction == 'left':
            pygame.draw.polygon(self.screen, Color.BLACK.value, [(x, y), (x + 10, y - 5), (x + 10, y + 5)])
        elif direction == 'right':
            pygame.draw.polygon(self.screen, Color.BLACK.value, [(x, y), (x - 10, y - 5), (x - 10, y + 5)])

    def run_menu(self):
        """Main menu loop for adjusting grid size and players."""
        while True:
            self.screen.fill((255, 255, 255))
            # Draw grid width and height
            self.draw_text(f'Grid Size: {self.grid_width} {self.grid_height}', 20, 20, Color.BLACK.value)
            self.draw_arrow(400, 30, 'left')
            self.draw_arrow(440, 30, 'right')

            self.draw_text(f'Number of Team: {self.num_team}', 20, 60, Color.BLACK.value)
            self.draw_arrow(400, 70, 'left')
            self.draw_arrow(440, 70, 'right')

            self.draw_text(f'Color of Team 1: {self.color[self.i].name}', 20, 100, self.color[self.i].value)
            self.draw_arrow(400, 110, 'left')
            self.draw_arrow(440, 110, 'right')

            self.draw_text(f'Color of Team 2: {self.color[self.j].name}', 20, 140, self.color[self.j].value)
            self.draw_arrow(400, 150, 'left')
            self.draw_arrow(440, 150, 'right')

            if self.num_team==3:
                self.draw_text(f'Color of Team 3: {self.color[self.k].name}', 20, 180, self.color[self.k].value)
                self.draw_arrow(400, 190, 'left')
                self.draw_arrow(440, 190, 'right')
            elif self.num_team==4:
                self.draw_text(f'Color of Team 3: {self.color[self.k].name}', 20, 180, self.color[self.k].value)
                self.draw_arrow(400, 190, 'left')
                self.draw_arrow(440, 190, 'right')
                self.draw_text(f'Color of Team 4: {self.color[self.l].name}', 20, 220, self.color[self.l].value)
                self.draw_arrow(400, 230, 'left')
                self.draw_arrow(440, 230, 'right')

            self.draw_text(f'Number of Agent per Team: {self.num_agent}', 20, 260, Color.BLACK.value)
            self.draw_arrow(400, 270, 'left')
            self.draw_arrow(440, 270, 'right')

            self.draw_text(f'nombre d\'obstacles: {self.nb_obs}', 20, 300, Color.BLACK.value)
            self.draw_arrow(400, 310, 'left')
            self.draw_arrow(440, 310, 'right')

            self.draw_text('Press Enter to Start', 20, 340, Color.BLACK.value)

            self.draw_text("Caution Two Different Team Can't Have The Same Color", 20, 380, Color.RED.value)
            self.alert=False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        #Check if two teams have the same color
                        if self.num_team==2 and self.i==self.j:
                            self.alert = True
                        elif self.num_team==3 and (self.i==self.j or self.i==self.k or self.k==self.j):
                            self.alert=True
                        elif self.num_team==4 and (self.i==self.j or self.i==self.k or self.i==self.l or self.j==self.k or self.j==self.l or self.k==self.l ):
                            self.alert = True
                        else:
                            # Exit the menu and return settings
                            return self.grid_width, self.grid_height, self.num_team, self.num_agent


                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos

                    # Check clicks for grid size
                    if 10 <= mouse_y <= 30:
                        if 390 <= mouse_x <= 410 and self.grid_width > 1:
                            self.grid_width -= 1
                            self.grid_height -= 1
                        elif 430 <= mouse_x <= 450 and self.grid_width < 40:
                            self.grid_width += 1
                            self.grid_height += 1

                    # Check clicks for number of team
                    if 50 <= mouse_y <= 70:
                        if 390 <= mouse_x <= 410 and self.num_team > 1:
                            self.num_team -= 1
                        elif 430 <= mouse_x <= 450 and self.num_team < 4:
                            self.num_team += 1

                    # Check clicks for color of team 1
                    if 90 <= mouse_y <= 110:
                        if 390 <= mouse_x <= 410 and self.i > 0:
                            self.i -= 1
                        elif 430 <= mouse_x <= 450 and self.i < len(self.color)-1:
                            self.i += 1

                    # Check clicks for color of team 2
                    if 130 <= mouse_y <= 150:
                        if 390 <= mouse_x <= 410 and self.j > 0:
                            self.j -= 1
                        elif 430 <= mouse_x <= 450 and self.j < len(self.color)-1:
                            self.j += 1

                    # Check clicks for color of team 3
                    if 170 <= mouse_y <= 190:
                        if 390 <= mouse_x <= 410 and self.k > 0:
                            self.k -= 1
                        elif 430 <= mouse_x <= 450 and self.k < len(self.color)-1:
                            self.k += 1

                    # Check clicks for color of team 4
                    if 210 <= mouse_y <= 230:
                        if 390 <= mouse_x <= 410 and self.l > 0:
                            self.l -= 1
                        elif 430 <= mouse_x <= 450 and self.l < len(self.color)-1:
                            self.l += 1

                    # Check clicks for number of agent per team
                    if 250 <= mouse_y <= 270:
                        if 390 <= mouse_x <= 410 and self.num_agent > 1:
                            self.num_agent -= 1
                        elif 430 <= mouse_x <= 450 and self.num_agent < 50:
                            self.num_agent += 1

                    if 290 <= mouse_y <= 310:
                        if 390 <= mouse_x <= 410 and self.nb_obs > 1:
                            self.nb_obs -= 1
                        elif 430 <= mouse_x <= 450 and self.nb_obs < 300:
                            self.nb_obs += 1

            pygame.display.flip()