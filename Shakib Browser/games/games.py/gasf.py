import pygame
import random

# Initialize Pygame
pygame.init()

# Set screen dimensions
screen_width = 640
screen_height = 480

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Define block size
block_size = 10

# Define clock for timing
clock = pygame.time.Clock()

# Define font for score display
font = pygame.font.SysFont(None, 25)

def snake(block_size, snake_list):
    for block in snake_list:
        pygame.draw.rect(screen, black, [block[0], block[1], block_size, block_size])

def message_to_screen(msg, color):
    screen_text = font.render(msg, True, color)
    screen.blit(screen_text, [screen_width/6, screen_height/3])

# Define main function
def gameLoop():
    # Initialize game variables
    gameExit = False
    gameOver = False

    # Define starting position of snake
    lead_x = screen_width / 2
    lead_y = screen_height / 2
    lead_x_change = 0
    lead_y_change = 0

    # Define starting position of food
    food_x = round(random.randrange(0, screen_width - block_size) / 10.0) * 10.0
    food_y = round(random.randrange(0, screen_height - block_size) / 10.0) * 10.0

    # Define snake list and starting length
    snake_list = []
    snake_length = 1

    # Start game loop
    while not gameExit:
        # If game over, prompt player to play again or quit
        while gameOver == True:
            screen.fill(white)
            message_to_screen("Game over, press Q to quit or C to play again", red)
            pygame.display.update()

            # Wait for player to select an option
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    elif event.key == pygame.K_c:
                        gameLoop()

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0

        # Check for collision with wall
        if lead_x >= screen_width or lead_x < 0 or lead_y >= screen_height or lead_y < 0:
            gameOver = True

        # Update snake position
        lead_x += lead_x_change
        lead_y += lead_y_change

        # Draw background and food
        screen.fill(white)
        pygame.draw.rect(screen, red, [food_x, food_y, block_size, block_size])

        # Add new snake block and remove old one
    snake_head = []
    snake_head.append(lead_x)
    snake_head.append(lead_y)
    snake_list.append(snake_head)

    if len(snake_list) > snake_length:
        del snake_list[0]

    # Check for collision with snake body
    for block in snake_list[:-1]:
        if block == snake_head:
            gameOver = True

    # Draw snake
    snake(block_size, snake_list)

    # Draw score
    score = snake_length - 1
    score_text = font.render("Score: " + str(score), True, black)
    screen.blit(score_text, [0, 0])

    # Update screen
    pygame.display.update()

    # Check for collision with food
    if lead_x == food_x and lead_y == food_y:
        food_x = round(random.randrange(0, screen_width - block_size) / 10.0) * 10.0
        food_y = round(random.randrange(0, screen_height - block_size) / 10.0) * 10.0
        snake_length += 1

    clock.tick(15)

# Quit Pygame
pygame.quit()
   # Set game speed
 
# Quit Python
quit()