import pygame

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGTH = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGTH))

FPS = 60

BALL_WIDTH = 30
BALL_HEIGTH = 30

ball_position = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
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
                run = False
                break

def draw():
    pygame.display.update()
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (ball_position.x, ball_position.y, BALL_WIDTH, BALL_HEIGTH))

def move():
    ball_position.x += 10
    ball_position.y += 10

    
start()        
update()

