import pygame

pygame.init()

width = 600
height = 600

screen = pygame.display.set_mode((width, height))

FPS = 60
BALL_WIDTH = 30
BALL_HEIGHT = 30

ball_position = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
ball_velocity = pygame.Vector2(6, 3)  
BLACK = (0, 0, 0)
AZURE = (0, 127, 255)


def start():
    pygame.display.set_caption("Prog Tutorial")


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
    pygame.draw.rect(
        screen, AZURE, (ball_position.x, ball_position.y, BALL_WIDTH, BALL_HEIGHT)
    )


def move():
    ball_position.x += ball_velocity.x
    ball_position.y += ball_velocity.y

    if ball_position.x <= 0 or ball_position.x >= 570:
        ball_velocity.x *= -1  

    if ball_position.y <= 0 or ball_position.y >= 570:
        ball_velocity.y *= -1  


start()
update()
