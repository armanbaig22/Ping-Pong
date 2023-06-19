import pygame

class Ball:
    def __init__(self, screen, pos, velocity):
        self.screen = screen
        self.pos = pos
        self.velocity = velocity

    def draw(self):
        pygame.draw.circle(self.screen, "white", (self.pos.x, self.pos.y), 10.0)

    def move(self, dt):
        speed = 950.0
        new_x = self.pos.x + self.velocity.x * speed * dt
        new_y = self.pos.y + self.velocity.y * speed * dt
        if new_y >= self.screen.get_height() - 10 or new_y <= 10:
            self.bounce_y()
            new_y = self.pos.y + self.velocity.y * speed * dt
        self.pos.x = new_x
        self.pos.y = new_y

    def bounce_x(self):
        self.velocity.x *= -1.0

    def bounce_y(self):
        self.velocity.y *= -1.0

    def reset_pos(self):
        self.pos.x = self.screen.get_width()/2
        self.pos.y = self.screen.get_height()/2

