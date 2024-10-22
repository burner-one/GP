# 2D TARGET SHOOTING GAME

import pygame
import random
import math
from pygame import mixer

# Initialize Pygame
pygame.init()

# Set up display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Shooter")
clock = pygame.time.Clock()

# Load background and fonts
background = pygame.image.load('Space.jpg')
score_val = 0
scoreX, scoreY = 5, 5
font = pygame.font.Font('freesansbold.ttf', 64)
game_over_font = pygame.font.Font('freesansbold.ttf', 64)

def show_score(x, y):
    score = font.render("Points:" + str(score_val), True, (255, 255, 255))
    screen.blit(score, (x, y))

def game_over():
    game_over_text = game_over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(game_over_text, (190, 255))
    mixer.music.load("music.mp3")
    mixer.music.play(-1)

# Load player and invader images
playerImage = pygame.image.load("NRG.png")
playerImage = pygame.transform.scale(playerImage, (75, 75))
player_X, player_Y = 370, 523
player_Xchange = 0

# Initialize invaders
invaderImage = []
invader_X = []
invader_Y = []
invader_Xchange = []
invader_Ychange = []
no_of_invaders = 8

for num in range(no_of_invaders):
    invaderImage.append(pygame.image.load("enemy.png"))
    invaderImage[num] = pygame.transform.scale(invaderImage[num], (65, 65))
    invader_X.append(random.randint(30, 737))
    invader_Y.append(random.randint(22, 180))
    invader_Xchange.append(1.2)
    invader_Ychange.append(30)

# Load bullet image
bulletImage = pygame.image.load("lazer.png")
bulletImage = pygame.transform.scale(bulletImage, (30, 45))
bullet_X, bullet_Y = 0, 50
bullet_Xchange = 0
bullet_Ychange = 3
bullet_state = "rest"

def isCollision(x1, x2, y1, y2):
    distance = math.sqrt((math.pow(x1 - x2, 2)) + (math.pow(y1 - y2, 2)))
    return distance <= 50

def player(x, y):
    screen.blit(playerImage, (x - 16, y + 10))

def invader(x, y, i):
    screen.blit(invaderImage[i], (x, y))

def bullet(x, y):
    global bullet_state
    screen.blit(bulletImage, (x, y))
    bullet_state = "fire"

# Main game loop
running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_Xchange = -1.7
            if event.key == pygame.K_RIGHT:
                player_Xchange = 1.7
            if event.key == pygame.K_SPACE and bullet_state == "rest":
                bullet_X = player_X
                bullet_Y = player_Y
                bullet_sound = mixer.Sound("lazer.mp3")
                bullet_sound.play()
        if event.type == pygame.KEYUP:
            player_Xchange = 0

    player_X += player_Xchange

    # Update invaders
    for i in range(no_of_invaders):
        invader_X[i] += invader_Xchange[i]
        
        if bullet_Y <= 0:
            bullet_Y = 600
            bullet_state = "rest"
        
        if bullet_state == "fire":
            bullet(bullet_X, bullet_Y)
            bullet_Y -= bullet_Ychange
        
        # Check for collisions
        collision = isCollision(bullet_X, invader_X[i], bullet_Y, invader_Y[i])
        if collision:
            score_val += 1
            bullet_Y = 600
            bullet_state = "rest"
            invader_Y[i] = 2000  # Move invader off screen
            explosion_sound = mixer.Sound("explosion.mp3")
            explosion_sound.play()
        
        if invader_X[i] >= 735 or invader_X[i] <= 0:
            invader_Xchange[i] *= -1
            invader_Y[i] += invader_Ychange[i]

        if invader_Y[i] >= 450 and abs(player_X - invader_X[i]) < 80:
            for j in range(no_of_invaders):
                invader_Y[j] = 2000  # Move all invaders off screen
            game_over()

        invader(invader_X[i], invader_Y[i], i)

    # Player boundaries
    if player_X <= 16:
        player_X = 16
    elif player_X >= 750:
        player_X = 750
    
    player(player_X, player_Y)
    show_score(scoreX, scoreY)
    clock.tick(120)
    pygame.display.update()
