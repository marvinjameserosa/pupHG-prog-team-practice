import pygame

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

FPS = 60

BALL_WIDTH = 30
BALL_HEIGHT = 30

ball_position = pygame.Vector2(screen.get_width() /2, screen.get_height() /2)
ball_velocity = pygame.Vector2(5, 2)

WHITE = (255, 255, 255)
BLACK = (0, 0 ,0)

def start():
    pygame.display.set_caption("Programming Basic Tutorial")

def update():
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        draw()
        move()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(pygame.QUIT)
                run = False
                break

def draw():
    pygame.display.update()
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (ball_position.x, ball_position.y, BALL_WIDTH, BALL_HEIGHT))

def move():
    ball_position.x += ball_velocity.x
    ball_position.y += ball_velocity.y

    
    if ball_position.x <= 0:
        ball_velocity.x = -ball_velocity.x #Change to opposite direction
    elif ball_position.x + BALL_WIDTH >= SCREEN_WIDTH: #Checks if Ball reaches right edge of screen
        ball_velocity.x = -ball_velocity.x

    if ball_position.y <= 0:
        ball_velocity.y = -ball_velocity.y  
    elif ball_position.y + BALL_HEIGHT >= SCREEN_HEIGHT: #Checks if Ball reaches bottom of the screen
        ball_velocity.y = -ball_velocity.y

start()
update()
        
        
