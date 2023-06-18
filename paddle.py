import pygame


class Paddle:
    def __init__(self, screen, player_pos):
        self.screen = screen
        self.player_pos = player_pos

    def draw(self):
        pygame.draw.polygon(self.screen, "white", [
            (self.player_pos.x, self.player_pos.y),
            (self.player_pos.x, self.player_pos.y + 100),
            (self.player_pos.x + 20, self.player_pos.y + 100),
            (self.player_pos.x + 20, self.player_pos.y)
        ])

    def go_up(self, dt):
        y_pos = self.player_pos.y
        mag = 2000
        if y_pos < 0:
            self.player_pos.y = 0
            return
        self.player_pos.y -= mag * dt

    def go_down(self, dt):
        mag = 2000
        y_pos = self.player_pos.y
        if y_pos > 500:
            self.player_pos.y = 500
            return
        self.player_pos.y += mag * dt
