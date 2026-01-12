import pygame
import time
import random

pygame.init()

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Window Size
window_width = 600
window_height = 400

# Create the display
game_display = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Snake Game')

# Clock
clock = pygame.time.Clock()

# Font
font_style = pygame.font.SysFont(None, 30)


def message(msg, color):
    """
    Display a message on the screen
    """
    message = font_style.render(msg, True, color)
    game_display.blit(message, [window_width / 6, window_height / 3])


def game_loop():
    """
    Main game loop
    """
    # Snake Size
    snake_block_size = 10

    # FPS (frames per second)
    fps = 20

    # Initial Direction
    direction = "right"

    # Snake's Starting Position
    x1 = window_width / 2
    y1 = window_height / 2

    # Food's Starting Position
    food_x = round(random.randrange(0, window_width - snake_block_size) / 10.0) * 10.0
    food_y = round(random.randrange(0, window_height - snake_block_size) / 10.0) * 10.0

    # Game Over Flag
    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            # Get key press
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = "left"
                elif event.key == pygame.K_RIGHT:
                    direction = "right"
                elif event.key == pygame.K_UP:
                    direction = "up"
                elif event.key == pygame.K_DOWN:
                    direction = "down"

        # Move the Snake
        if direction == "right":
            x1 += snake_block_size
        elif direction == "left":
            x1 -= snake_block_size
        elif direction == "up":
            y1 -= snake_block_size
        elif direction == "down":
            y1 += snake_block_size

        # Check if Snake hit the wall
        if x1 >= window_width or x1 < 0 or y1 >= window_height or y1 < 0:
            game_over = True

        # Fill the display with white color
        game_display.fill(white)

        # Draw the Food
        pygame.draw.rect(game_display, blue, [food_x, food_y, snake_block_size, snake_block_size])

        # Draw the Snake
        snake_head = [x1, y1]
        snake_list = [snake_head]

        pygame.draw.rect(game_display, black, [x1, y1, snake_block_size, snake_block_size])

        # Update the display
        pygame.display.update()

        # Check if the Snake hit the food
        if x1 == food_x and y1 == food_y:
            print("Yummy!!")
            time
