import pygame
import random

# Initialize Pygame
pygame.init()

# Set screen size
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

# Set colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set font
font = pygame.font.SysFont(None, 25)

# Set clock
clock = pygame.time.Clock()

# Set snake variables
SNAKE_SIZE = 10
snake_x = SCREEN_WIDTH / 2
snake_y = SCREEN_HEIGHT / 2
snake_x_change = 0
snake_y_change = 0
snake_body = []

# Set food variables
FOOD_SIZE = 10
food_x = round(random.randrange(0, SCREEN_WIDTH - FOOD_SIZE) / 10.0) * 10.0
food_y = round(random.randrange(0, SCREEN_HEIGHT - FOOD_SIZE) / 10.0) * 10.0

# Set game variables
game_over = False
score = 0
high_score = 0
speed = 10

# Set screen mode variables
FULL_SCREEN = False

# Function to draw snake
def draw_snake(snake_body):
    for body_part in snake_body:
        pygame.draw.rect(screen, GREEN, [body_part[0], body_part[1], SNAKE_SIZE, SNAKE_SIZE])

# Function to display score
def show_score(score, high_score):
    score_text = font.render("Score: " + str(score), True, WHITE)
    high_score_text = font.render("High Score: " + str(high_score), True, WHITE)
    screen.blit(score_text, [10, 10])
    screen.blit(high_score_text, [10, 30])

# Function to toggle full screen mode
def toggle_full_screen():
    global FULL_SCREEN, screen
    FULL_SCREEN = not FULL_SCREEN
    if FULL_SCREEN:
        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    else:
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Game loop
while not game_over:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_x_change = -SNAKE_SIZE
                snake_y_change = 0
            elif event.key == pygame.K_RIGHT:
                snake_x_change = SNAKE_SIZE
                snake_y_change = 0
            elif event.key == pygame.K_UP:
                snake_y_change = -SNAKE_SIZE
                snake_x_change = 0
            elif event.key == pygame.K_DOWN:
                snake_y_change = SNAKE_SIZE
                snake_x_change = 0
            elif event.key == pygame.K_f:
                toggle_full_screen()

    # Move snake
    snake_x += snake_x_change
    snake_y += snake_y_change

    # Check for collision with wall
    if snake_x < 0 or snake_x >= SCREEN_WIDTH or snake_y < 0 or snake_y >= SCREEN_HEIGHT:
        game_over = True

    # Check for collision with food
    if snake_x == food_x and snake_y == food_y:
        food_x = round(random.randrange(0, SCREEN_WIDTH - FOOD_SIZE) / 10.0) *10.0
        food_y = round(random.randrange(0, SCREEN_HEIGHT - FOOD_SIZE) / 10.0) * 10.0
    score += 1
    speed += 1

    # Update high score
    if score > high_score:
        high_score = score

# Add new body part to snake
snake_body.append([snake_x, snake_y])

# Remove tail of snake
if len(snake_body) > score:
    del snake_body[0]

# Fill screen
screen.fill(BLACK)

# Draw food
pygame.draw.rect(screen, RED, [food_x, food_y, FOOD_SIZE, FOOD_SIZE])

# Draw snake
draw_snake(snake_body)

# Display score
show_score(score, high_score)

# Update screen
pygame.display.update()

# Set FPS based on speed
clock.tick(speed)

