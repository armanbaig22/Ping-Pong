import pygame

class ScoreBoard:
    def __init__(self, screen):
        self.screen = screen
        self.l_score = 0
        self.r_score = 0
        self.font = pygame.font.SysFont("Consolas", 50)
        self.update()

    def update(self):
        l_score_text = self.font.render(str(self.l_score), True, (255, 255, 255))
        r_score_text = self.font.render(str(self.r_score), True, (255, 255, 255))
        
        l_score_rect = l_score_text.get_rect()
        r_score_rect = r_score_text.get_rect()

        l_score_rect.center = (self.screen.get_width() / 2 - 50, 50)
        r_score_rect.center = (self.screen.get_width() / 2 + 50, 50)
        # draw the score_text on the screen at score_rect
        self.screen.blit(l_score_text, l_score_rect)
        self.screen.blit(r_score_text, r_score_rect)

    def l_point(self):
        self.l_score += 1
        self.update()

    def r_point(self):
        self.r_score += 1
        self.update()


