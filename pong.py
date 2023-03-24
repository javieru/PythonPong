import pygame
import sys

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 60
BALL_SIZE = 10
PADDLE_SPEED = 5
BALL_SPEED = 2

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Pong')

# Define the paddles and ball
left_paddle = pygame.Rect(20, SCREEN_HEIGHT // 2 -
                          PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
right_paddle = pygame.Rect(SCREEN_WIDTH - 30, SCREEN_HEIGHT //
                           2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(SCREEN_WIDTH // 2 - BALL_SIZE // 2,
                   SCREEN_HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)

# Ball movement
ball_dx = BALL_SPEED
ball_dy = BALL_SPEED

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and right_paddle.top > 0:
        right_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and right_paddle.bottom < SCREEN_HEIGHT:
        right_paddle.y += PADDLE_SPEED
    if keys[pygame.K_w] and left_paddle.top > 0:
        left_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_s] and left_paddle.bottom < SCREEN_HEIGHT:
        left_paddle.y += PADDLE_SPEED

    # Ball movement
    ball.x += ball_dx
    ball.y += ball_dy

    # Ball collision with paddles
    if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
        ball_dx = -ball_dx

    # Ball collision with top and bottom screen boundaries
    if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
        ball_dy = -ball_dy

    # Ball out of bounds
    if ball.left <= 0 or ball.right >= SCREEN_WIDTH:
        ball.x = SCREEN_WIDTH // 2 - BALL_SIZE // 2
        ball.y = SCREEN_HEIGHT // 2 - BALL_SIZE // 2
        ball_dx = BALL_SPEED

    # Draw the paddles and ball
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, left_paddle)
    pygame.draw.rect(screen, WHITE, right_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (SCREEN_WIDTH // 2, 0),
                       (SCREEN_WIDTH // 2, SCREEN_HEIGHT))

    # Update the display
    pygame.display.flip()
    pygame.time.delay(10)
