import pygame
from paddle import Paddle
from ball import Ball
from score import ScoreBoard
from line import Line
from menu import Menu

# Initialize pygame
pygame.init()


# Function to initialize the game
def initialize_game():
    # Set up the window
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Pong')
    clock = pygame.time.Clock()
    running = True
    dt = 0

    # Load sound effects
    bounce_sound = pygame.mixer.Sound('sounds/bounce.wav')
    score_sound = pygame.mixer.Sound('sounds/score.wav')

    # Initialize positions and velocities
    paddle1_pos = pygame.Vector2(10, screen.get_height() / 2 - 50)
    paddle2_pos = pygame.Vector2(screen.get_width() - 30, screen.get_height() / 2 - 50)
    ball_pos = pygame.Vector2(screen.get_width() / 2 - 200, screen.get_height() / 2 - 200)
    ball_velocity = pygame.Vector2(1, 1)

    # Create objects
    menu = Menu(screen)
    scoreboard = ScoreBoard(screen)
    line = Line(screen)

    # Initialize paddles and ball
    paddle1 = Paddle(screen, paddle1_pos)
    paddle2 = Paddle(screen, paddle2_pos)
    ball = Ball(screen, ball_pos, ball_velocity)

    return screen, clock, running, dt, bounce_sound, score_sound, \
        paddle1, paddle2, ball, menu, scoreboard, line


# Main game loop
def main():
    screen, clock, running, dt, bounce_sound, score_sound, \
        paddle1, paddle2, ball, menu, scoreboard, line = initialize_game()

    menu.draw()
    menu.hold()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("black")
        line.draw()
        paddle1.draw()
        paddle2.draw()
        ball.draw()
        ball.move(dt)

        # Check collision with top and bottom walls
        if ball.pos.y >= screen.get_height() - 10 or ball.pos.y <= 10:
            ball.bounce_y()
            bounce_sound.play()  # Play bounce sound effect

        # Conditions to check collision with paddles
        if 40 >= ball.pos.x > 20 and 0 <= ball.pos.y - paddle1.player_pos.y < 100:
            ball.pos.x = 40
            ball.bounce_x()
            bounce_sound.play()  # Play bounce sound effect

        if screen.get_width() - 40 <= ball.pos.x < screen.get_width() - 20 and 0 <= ball.pos.y - paddle2.player_pos.y < 100:
            ball.pos.x = screen.get_width() - 40
            ball.bounce_x()
            bounce_sound.play()  # Play bounce sound effect

        # Conditions to check if ball is out of bounds
        if ball.pos.x >= 800:
            scoreboard.l_point()
            ball.reset_pos()
            score_sound.play()  # Play score sound effect

        if ball.pos.x <= 0:
            scoreboard.r_point()
            ball.reset_pos()
            score_sound.play()  # Play score sound effect

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


if __name__ == "__main__":
    main()
