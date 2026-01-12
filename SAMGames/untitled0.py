import pygame
import random

# initialize Pygame
pygame.init()

# set up the game window
win_width = 600
win_height = 400
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Snake Game")

# set up the clock
clock = pygame.time.Clock()

# define game constants
block_size = 20
font = pygame.font.SysFont(None, 30)

# define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# define the snake class
class Snake:
    def __init__(self, x, y):
        self.segments = [(x, y)]
        self.dx = block_size
        self.dy = 0
    
    def move(self):
        x, y = self.segments[0]
        x += self.dx
        y += self.dy
        self.segments.insert(0, (x, y))
        self.segments.pop()
    
    def grow(self):
        x, y = self.segments[0]
        x += self.dx
        y += self.dy
        self.segments.insert(0, (x, y))
    
    def draw(self, surface):
        for segment in self.segments:
            pygame.draw.rect(surface, white, (segment[0], segment[1], block_size, block_size))

# define the food class
class Food:
    def __init__(self):
        self.x = random.randint(0, (win_width - block_size) // block_size) * block_size
        self.y = random.randint(0, (win_height - block_size) // block_size) * block_size
    
    def draw(self, surface):
        pygame.draw.rect(surface, red, (self.x, self.y, block_size, block_size))

# create the snake and food objects
snake = Snake(0, 0)
food = Food()

# game loop
running = True
while running:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake.dx = -block_size
                snake.dy = 0
            elif event.key == pygame.K_RIGHT:
                snake.dx = block_size
                snake.dy = 0
            elif event.key == pygame.K_UP:
                snake.dy = -block_size
                snake.dx = 0
            elif event.key == pygame.K_DOWN:
                snake.dy = block_size
                snake.dx = 0
    
    # update game state
    snake.move()
    if snake.segments[0][0] == food.x and snake.segments[0][1] == food.y:
        food = Food()
        snake.grow()
    if (
        snake.segments[0][0] < 0 or
        snake.segments[0][0] >= win_width or
        snake.segments[0][1] < 0 or
        snake.segments[0][1] >= win_height or
        snake.segments[0] in snake.segments[1:]
    ):
        running = False
    
    # draw game objects
    win.fill(black)
    snake.draw(win)
    food.draw(win)
    score_text = font.render("Score: " + str(len(snake.segments) - 1), True, white)
    win.blit(score_text, (10, 10))
    pygame.display.update()
    
    # control the frame rate
    clock.tick(10)

# quit Pygame
pygame.quit
