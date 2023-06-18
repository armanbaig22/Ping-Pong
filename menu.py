import pygame
import sys

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont("Consolas", 60)
        self.title = "PONG"
        self.button_font = pygame.font.SysFont("Arial", 40)
        self.button_text = "Start"
        self.button_rect = pygame.Rect(0, 0, 200, 50)
        self.button_rect.center = (self.screen.get_width() // 2, self.screen.get_height() // 2 + 50)

    def draw(self):
        self.screen.fill((0, 0, 0))  # Clear the screen with black color

        # Render and display the "PONG" title
        title_text = self.font.render(self.title, True, (255, 255, 255))
        title_rect = title_text.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2 - 100))
        self.screen.blit(title_text, title_rect)

        # Render and display the "Start" button
        pygame.draw.rect(self.screen, (255, 255, 255), self.button_rect)
        button_text = self.button_font.render(self.button_text, True, (0, 0, 0))
        button_text_rect = button_text.get_rect(center=self.button_rect.center)
        self.screen.blit(button_text, button_text_rect)

    def hold(self):
        while True:
            self.draw()
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.button_rect.collidepoint(event.pos):
                        return
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
