import pygame
import sys
import random

# --- SETUP ---
pygame.init()

WIDTH, HEIGHT = 1000, 750
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

clock = pygame.time.Clock()

# COLORS
SKY = (135, 206, 235)
BIRD_COLOR = (255, 175, 33)
PIPE_COLOR = (15, 175, 15)

# GAME CONSTANTS
GRAVITY = 0.5
JUMP = -8
PIPE_SPEED = 5
PIPE_GAP = 150

# --- GAME STATE ---
bird = pygame.Rect(470, 370, 50, 50)
bird_velocity = 0


def create_pipes():
    height = random.randint(50, 500)
    top = pygame.Rect(WIDTH - 50, 0, 75, height)
    bottom = pygame.Rect(WIDTH - 50, height + PIPE_GAP, 75, HEIGHT - height - PIPE_GAP)
    return top, bottom


def reset_game():
    global bird_velocity, pipe1, pipe2

    pygame.time.wait(1000)

    bird.center = (WIDTH // 2, HEIGHT // 2)
    bird_velocity = 0
    pipe1, pipe2 = create_pipes()


pipe1, pipe2 = create_pipes()

# --- MAIN LOOP ---
running = True
while running:
    # EVENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bird_velocity = JUMP

    # BIRD PHYSICS
    bird_velocity += GRAVITY
    bird.y += bird_velocity

    if bird.top <= 0:
        bird.top = 0
        bird_velocity = 0

    if bird.bottom >= HEIGHT:
        bird.bottom = HEIGHT
        reset_game()

    # PIPES MOVEMENT
    pipe1.x -= PIPE_SPEED
    pipe2.x -= PIPE_SPEED

    if pipe1.right < 0:
        pipe1, pipe2 = create_pipes()

    # COLLISION
    if bird.colliderect(pipe1) or bird.colliderect(pipe2):
        reset_game()

    # DRAW
    screen.fill(SKY)
    pygame.draw.ellipse(screen, BIRD_COLOR, bird)
    pygame.draw.rect(screen, PIPE_COLOR, pipe1)
    pygame.draw.rect(screen, PIPE_COLOR, pipe2)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()