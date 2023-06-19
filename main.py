import pygame
from paddle import Paddle
from ball import Ball
from score import ScoreBoard
from line import Line
from menu import Menu
# Initialize pygame
pygame.init()

# Set up the window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Pong')
clock = pygame.time.Clock()
running = True
dt = 0

paddle1_pos = pygame.Vector2(10, screen.get_height() / 2 - 50)
paddle2_pos = pygame.Vector2(screen.get_width() - 30, screen.get_height() / 2 - 50)
ball_pos = pygame.Vector2(screen.get_width() / 2 - 200, screen.get_height() / 2 - 200)
ball_velocity = pygame.Vector2(1, 1)

# main menu
menu = Menu(screen)
menu.draw()
menu.hold()

scoreboard = ScoreBoard(screen)  # Create ScoreBoard instance outside the game loop
line = Line(screen)
line.draw()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")
    line = Line(screen)
    line.draw()
    paddle1 = Paddle(screen, paddle1_pos)
    paddle1.draw()
    paddle2 = Paddle(screen, paddle2_pos)
    paddle2.draw()

    ball = Ball(screen, ball_pos, ball_velocity)
    ball.draw()
    ball.move(dt)

    # check collision with top and bottom walls

    if ball.pos.y >= screen.get_height()-10 or ball.pos.y <= 10:
        ball.bounce_y()

    # conditions to check collision with paddles

    if 40 >= ball.pos.x > 20 and 0 <= ball.pos.y - paddle1_pos.y < 100:
        ball.pos.x = 40
        ball.bounce_x()

    if screen.get_width() - 40 <= ball.pos.x < screen.get_width() - 20 and 0 <= ball.pos.y - paddle2_pos.y < 100:
        ball.pos.x = screen.get_width() - 40
        ball.bounce_x()

    # conditions to check if ball is out of bounds

    if ball.pos.x >= 800:
        scoreboard.l_point()
        ball.reset_pos()

    if ball.pos.x <= 0:
        scoreboard.r_point()
        ball.reset_pos()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        paddle1.go_up(dt)
    if keys[pygame.K_s]:
        paddle1.go_down(dt)
    if keys[pygame.K_UP]:
        paddle2.go_up(dt)
    if keys[pygame.K_DOWN]:
        paddle2.go_down(dt)

    scoreboard.update()

    pygame.display.flip()
    dt = clock.tick(2000) / 2000

pygame.quit()



