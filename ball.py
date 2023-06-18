import pygame

class Ball:
    def __init__(self, screen, pos, velocity):
        self.screen = screen
        self.pos = pos
        self.velocity = velocity

    def draw(self):
        pygame.draw.circle(self.screen, "white", (int(self.pos.x), int(self.pos.y)), 10)

    def move(self, dt):
        speed = 950
        new_x = self.pos.x + self.velocity.x * speed * dt
        new_y = self.pos.y + self.velocity.y * speed * dt
        self.pos.x = new_x
        self.pos.y = new_y

    def bounce_x(self):
        new_x = self.velocity.x * -1.0
        self.velocity.x = new_x

    def bounce_y(self):
        new_y = self.velocity.y * -1.0
        self.velocity.y = new_y

    def reset_pos(self):
        self.pos.x = 400
        self.pos.y = 300

