import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong Game Made By Hemotogenas! https://github.com/Hemotogenas")

# Game objects
ball = pygame.Rect(WIDTH // 2 - 10, HEIGHT // 2 - 10, 20, 20)
human = pygame.Rect(WIDTH - 20, HEIGHT // 2 - 60, 10, 120)
bot = pygame.Rect(10, HEIGHT // 2 - 60, 10, 120)

# Initial ball speed
ball_speed = [5, 5]

# Initial scores
human_score = 0
bot_score = 0

# Fonts
font = pygame.font.Font(None, 36)

# Game loop
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and human.top > 0:
        human.y -= 5
    if keys[pygame.K_DOWN] and human.bottom < HEIGHT:
        human.y += 5

    # Update game objects
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    # Ball collisions
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed[1] = -ball_speed[1]

    if ball.colliderect(human) or ball.colliderect(bot):
        ball_speed[0] = -ball_speed[0]

    # Bot AI
    if bot.centery < ball.centery:
        bot.y += 3
    elif bot.centery > ball.centery:
        bot.y -= 3

    # Score handling
    if ball.right >= WIDTH and not human.colliderect(ball):
        bot_score += 1
        ball.x = WIDTH // 2 - 10
        ball.y = HEIGHT // 2 - 10
    elif ball.left <= 0 and not bot.colliderect(ball):
        human_score += 1
        ball.x = WIDTH // 2 - 10
        ball.y = HEIGHT // 2 - 10

    # Draw everything
    screen.fill(BLACK)

    # Draw scores
    human_text = font.render("Human : " + str(human_score), True, WHITE)
    bot_text = font.render("Bot: " + str(bot_score), True, WHITE)
    screen.blit(human_text, (WIDTH - 150, 10))
    screen.blit(bot_text, (10, 10))

    pygame.draw.rect(screen, WHITE, human)
    pygame.draw.rect(screen, WHITE, bot)
    pygame.draw.ellipse(screen, WHITE, ball)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

    # Check for game over (reset) condition
    if human_score == 5 or bot_score == 5:
        human_score = 0
        bot_score = 0
