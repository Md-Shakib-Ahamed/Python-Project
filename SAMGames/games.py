import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")

# Set up the colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Set up the game clock
clock = pygame.time.Clock()

# Set up the snake
snake_size = 10
snake_speed = 15
direction = "right"

def draw_snake(snake_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(window, black, [x[0], x[1], snake_size, snake_size])

# Set up the main game loop
def game_loop():
    game_over = False
    game_close = False

    x1 = window_width / 2
    y1 = window_height / 2

    x1_change = 0       
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, window_width - snake_size) / 10.0) * 10.0
    foody = round(random.randrange(0, window_height - snake_size) / 10.0) * 10.0

    # Start the game loop
    while not game_over:

        while game_close == True:
            window.fill(white)
            font_style = pygame.font.SysFont(None, 50)
            message = font_style.render("You lost! Press Q-Quit or C-Play Again", True, red)
            window.blit(message, [window_width / 6, window_height / 3])
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = "left"
                    x1_change = -snake_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    direction = "right"
                    x1_change = snake_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    direction = "up"
                    y1_change = -snake_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    direction = "down"
                    y1_change = snake_size
                    x1_change = 0

        # Check for boundaries
        if x1 >= window_width or x1 < 0 or y1 >= window_height or y1 < 0:
            game_close = True

        # Update snake position
        x1 += x1_change
        y1 += y1_change
        window.fill(white)
        pygame.draw.rect(window, red, [foodx, foody, snake_size, snake_size])

        
                # Add to snake length if food is eaten
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        draw_snake(snake_size, snake_List)
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, window_width - snake_size) / 10.0) * 10.0
            foody = round(random.randrange(0, window_height - snake_size) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop()

