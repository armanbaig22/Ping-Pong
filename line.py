import pygame

class Line:
    def __init__(self, screen):
        self.screen = screen

    def draw(self):
        start = 0
        end = 15
        for i in range(0, 20):
            pygame.draw.line(self.screen, "white", (self.screen.get_width()/2, start), (self.screen.get_width()/2, end), 5)
            start += 40
            end += 40
