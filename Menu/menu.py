import pygame
import sys

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)
        self.grid_width = 10
        self.grid_height = 10
        self.num_team = 2  # Default number of team
        self.num_agent = 2

    def draw_text(self, text, x, y):
        text_surface = self.font.render(text, True, (0, 0, 0))
        self.screen.blit(text_surface, (x, y))

    def draw_arrow(self, x, y, direction):
        """Draws a left or right arrow."""
        if direction == 'left':
            pygame.draw.polygon(self.screen, (0, 0, 0), [(x, y), (x + 10, y - 5), (x + 10, y + 5)])
        elif direction == 'right':
            pygame.draw.polygon(self.screen, (0, 0, 0), [(x, y), (x - 10, y - 5), (x - 10, y + 5)])

    def run_menu(self):
        """Main menu loop for adjusting grid size and players."""
        while True:
            self.screen.fill((255, 255, 255))

            # Draw grid width and height
            self.draw_text(f'Grid Width: {self.grid_width}', 20, 20)
            self.draw_arrow(370, 25, 'left')
            self.draw_arrow(410, 25, 'right')


            self.draw_text(f'Grid Height: {self.grid_height}', 20, 60)
            self.draw_arrow(370, 65, 'left')
            self.draw_arrow(410, 65, 'right')

            self.draw_text(f'Number of Team: {self.num_team}', 20, 100)
            self.draw_arrow(370, 105, 'left')
            self.draw_arrow(410, 105, 'right')

            self.draw_text(f'Number of agent per team: {self.num_agent}', 20, 140)
            self.draw_arrow(370, 145, 'left')
            self.draw_arrow(410, 145, 'right')

            self.draw_text('Press Enter to Start', 20, 170)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        # Exit the menu and return settings
                        return self.grid_width, self.grid_height, self.num_team, self.num_agent

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos

                    # Check clicks for grid width
                    if 10 <= mouse_y <= 30:
                        if 360 <= mouse_x <= 290 and self.grid_width > 1:
                            self.grid_width -= 1
                        elif 400 <= mouse_x <= 420 and self.grid_width < 20:
                            self.grid_width += 1

                    # Check clicks for grid height
                    if 50 <= mouse_y <= 70:
                        if 360 <= mouse_x <= 380 and self.grid_height > 1:
                            self.grid_height -= 1
                        elif 400 <= mouse_x <= 420 and self.grid_height < 20:
                            self.grid_height += 1

                    # Check clicks for number of team
                    if 90 <= mouse_y <= 110:
                        if 360 <= mouse_x <= 380 and self.num_team > 1:
                            self.num_team -= 1
                        elif 400 <= mouse_x <= 420 and self.num_team < 4:
                            self.num_team += 1

                    # Check clicks for number of agent per
                    if 130 <= mouse_y <= 150:
                        if 360 <= mouse_x <= 380 and self.num_agent > 1:
                            self.num_agent -= 1
                        elif 400 <= mouse_x <= 420 and self.num_agent < 20:
                            self.num_agent += 1

            pygame.display.flip()