import pygame
import time
import random

# initialize pygame
pygame.init()

# set the display size
display_width = 800
display_height = 600

# set the colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# set the block size
snake_block = 10

# set the font size
font_style = pygame.font.SysFont(None, 30)
# create the game display
gameDisplay = pygame.display.set_mode((display_width, display_height))

# define a function to display the message
def message(msg, color):
    msg = font_style.render(msg, True, color)
    gameDisplay.blit(msg, [display_width/6, display_height/3])

# define the game loop
def gameLoop():
    # set the game variables
    game_over = False
    game_close = False

    # set the starting position of the snake
    x1 = display_width / 2
    y1 = display_height / 2

    # set the change in position of the snake
    x1_change = 0       
    y1_change = 0

    # generate the location of the food
    foodx = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0

    # set the clock
    clock = pygame.time.Clock()

    # create the game display
    gameDisplay = pygame.display.set_mode((display_width, display_height))

    # set the game caption
    pygame.display.set_caption('Snake game')

    # initialize the snake list
    snake_List = []
    Length_of_snake = 1

    # set the snake speed
    snake_speed = 15

    # start the game loop
    while not game_over:

        # if the game has ended
        while game_close == True:
            gameDisplay.fill(white)
            message('You lost! Press Q-Quit or C-Play Again', red)
            pygame.display.update()

            # wait for user input
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        # handle user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # move the snake
        x1 += x1_change
        y1 += y1_change

        # check if the snake has collided with the food
        if x1 == foodx and y1 == foody:foodx = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0
        Length_of_snake += 1

    # draw the snake
    snake_Head = []
    snake_Head.append(x1)
    snake_Head.append(y1)
    snake_List.append(snake_Head)
    if len(snake_List) > Length_of_snake:
        del snake_List[0]

    for x in snake_List[:-1]:
        if x == snake_Head:
            game_close = True

    # update the display
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_over = True

    gameDisplay.fill(white)

    # draw the snake
    for x in snake_List:
        pygame.draw.rect(gameDisplay, black, [x[0], x[1], snake_block, snake_block])

    # draw the food
    pygame.draw.rect(gameDisplay, red, [foodx, foody, snake_block, snake_block])

    # update the snake's position
    pygame.display.update()

    # check if the snake has hit the boundaries
    if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0:
        game_close = True

    # increase the snake's speed as it gets longer
    if Length_of_snake > 1:
        snake_speed = 15 + int(Length_of_snake / 5)

    # move the snake
    x1 += x1_change
    y1 += y1_change

    # set the game speed
    clock.tick(snake_speed)

# uninitialize pygame
pygame.quit()

# quit the program
quit()

