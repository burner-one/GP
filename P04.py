import pygame import 
random import math from 
pygame import mixer  
  
pygame.init()  
  
screen_width = 800 screen_height = 600 screen = 
pygame.display.set_mode((screen_width, screen_height))  
clock = pygame.time.Clock()    
pygame.display.set_caption("space shooter")  
background = pygame.image.load('Space.jpg')    
score_val = 0 
scoreX = 5 scoreY 
= 5  
font = pygame.font.Font('freesansbold.ttf', 64)  
game_over_font = pygame.font.Font('freesansbold.ttf', 64)  
def show_score(x, y):  
score = font.render("Points:"+str(score_val),  
True, (255,255,255))  
screen.blit(score, (x, y))  
def game_over():  
game_over_text = game_over_font.render("GAME OVER",  
True, (255,255,255))     
screen.blit(game_over_text,(190, 255))  
mixer.music.load("music.mp3") mixer.music.play(-1)  
playerImage = pygame.image.load("NRG.png") playerImage 
= pygame.transform.scale(playerImage, (75, 75))  player_X = 
370 player_Y = 523 player_Xchange = 0  
invaderImage = [] 
invader_X = [] invader_Y 
= [] invader_Xchange = 
[] invader_Ychange = [] 
no_of_invaders = 8  
for num in range(no_of_invaders):  
invaderImage.append(pygame.image.load("enemy.png"))     
invaderImage[num] = pygame.transform.scale(invaderImage[num], (65, 65))     
invader_X.append(random.randint(30, 737))     
invader_Y.append(random.randint(22, 180))     invader_Xchange.append(1.2)     
invader_Ychange.append(30)  
bulletImage = pygame.image.load("lazer.png") bulletImage 
= pygame.transform.scale(bulletImage, (30, 45))  bullet_X = 
0 bullet_Y = 50 bullet_Xchange = 0 bullet_Ychange = 3 
bullet_state = "rest"  
def isCollision(x1, x2, y1, y2):  
distance = math.sqrt((math.pow(x1 - x2,2)) +  
(math.pow(y1 - y2,2)))     
if distance <= 50:         return True     
else:  
return False  
def player(x, y):  
screen.blit(playerImage,(x - 16, y + 10))  
def invader(x, y, i):  
screen.blit(invaderImage[i], (x, y))  
def bullet(x, y):     global 
bullet_state     
screen.blit(bulletImage, (x, y))     
bullet_state = "fire"  
running = True while 
running:     
screen.fill((0,0,0))     
screen.blit(backgrou
 nd, (0, 0))
 event in 
        for 
pygame.event.get():         
if event.type == 
pygame.QUIT:  
running = False  
if event.type == pygame.KEYDOWN:             
if event.key == pygame.K_LEFT:  
player_Xchange = -1.7             if 
event.key == pygame.K_RIGHT:  
player_Xchange = 1.7             if event.key == 
pygame.K_SPACE:         
bullet_X = player_X       
bullet_Y) 
        if bullet_state == "rest":                     
              bullet(bullet_X, 
                    bullet_sound = mixer.Sound("lazer
mp3.mp3")                     bullet_sound.play()
 event.type == pygame.KEYUP:  
player_Xchange = 0  
player_X += player_Xchange     
         if 
for i in range(no_of_invaders):  
invader_X[i] += invader_Xchange[i]  
if bullet_Y <= 0:         
bullet_Y = 600         bullet_state 
= "rest"
 "fire":
 bullet_Y) 
     if bullet_state == 
         bullet(bullet_X, 
        bullet_Y -= 
bullet_Ychange     for i in 
range(no_of_invaders):   
invader_Y[i] >= 450:             
      if 
if 
abs(player_X-invader_X[i]) < 
80:                 for j in 
range(no_of_invaders):  
invader_Y[j] = 2000                     explosion_sound 
= mixer.Sound("explosion.mp3")                     
explosion_sound.play()   
              game_over()      
if invader_X[i] >= 735 or invader_X[i] <= 0:  
invader_Xchange[i] *= -1             
invader_Y[i] += invader_Ychange[i]
 = isCollision(bullet_X, invader_X[i],                                 
bullet_Y, invader_Y[i])   
score_val += 1     
      if collision:  
         collision 
        bullet_Y = 600             
bullet_state = "rest"
 random.randint(64,736)  
random.randint(30,200)             
invader_Xchange[i] *= -1  
             invader_X[i] = 
           invader_Y[i] = 
invader(invader_X[i], invader_Y[i], i)  
           break  
if player_X <= 16:         
player_X = 16;     elif 
player_X >= 750:         
player_X = 750     
player(player_X, 
player_Y)     
show_score(scoreX, 
scoreY)     
clock.tick(120) 
pygame.display.update(
 ) 
