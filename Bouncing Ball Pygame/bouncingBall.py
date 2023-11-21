import pygame

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

FPS = 60

BALL_WIDTH = 60
BALL_HEIGHT = 60

ball_position = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
ball_speed = pygame.Vector2(1, 1)  

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def start():
    pygame.display.set_caption("Bouncing Ball")


def update():
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        move()
        draw()


def draw():
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (ball_position.x, ball_position.y, BALL_WIDTH, BALL_HEIGHT))
    pygame.display.flip()


def move():
    
    ball_position.x += ball_speed.x
    ball_position.y += ball_speed.y

    
    if ball_position.x <= 0 or ball_position.x + BALL_WIDTH >= SCREEN_WIDTH:
        ball_speed.x = -ball_speed.x
    if ball_position.y <= 0 or ball_position.y + BALL_HEIGHT >= SCREEN_HEIGHT:
        ball_speed.y = -ball_speed.y


start()
update()
