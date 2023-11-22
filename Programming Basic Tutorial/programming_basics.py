import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

FPS = 60

BALL_WIDTH = 50
BALL_HEIGHT = 50

ball_position = pygame.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
ball_speed = pygame.Vector2(-3, 3)  # Initial speed
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def start():
    pygame.display.set_caption("Programming Basic Tutorial")

def update():
    run = True
    clock = pygame.time.Clock()
    move_ball = False 

    while run:
        clock.tick(FPS)
        draw()
        move_ball = handle_movement(move_ball)
        move(move_ball)
        if bounce(move_ball):
            reset_game(move_ball)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        

def handle_movement(move_ball):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if move_ball:
                reset_game(move_ball)
            else:
                move_ball
            return not move_ball 

    return move_ball

def draw():
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, (int(ball_position.x), int(ball_position.y), BALL_WIDTH, BALL_HEIGHT))
    pygame.display.update()

def move(move_ball):
    if move_ball:
        ball_position.x += ball_speed.x
        ball_position.y += ball_speed.y

def bounce(move_ball):
    if ball_position.y <= 0 or ball_position.y + BALL_HEIGHT >= SCREEN_HEIGHT:
        ball_speed.y *= -1
        

    if ball_position.x <= 0 or ball_position.x + BALL_WIDTH >= SCREEN_WIDTH:
        ball_speed.x *= -1

        if not move_ball:
            return True  

def reset_game():
    ball_position.x = SCREEN_WIDTH / 2
    ball_position.y = SCREEN_HEIGHT / 2

start()
update()
