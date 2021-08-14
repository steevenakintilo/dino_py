#!/usr/bin/env python3
##
## EPITECH PROJECT, 2021
## d
## File description:
## d
##

# Import the pygame module
import pygame
from random import randint
import pygame.freetype 
# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    K_SPACE,
    KEYDOWN,
    QUIT,
)

# Define constants for the screen width and height
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.Surface((20, 10))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = random.randint(5, 20)
# Define a player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
class Player(pygame.sprite.Sprite):
    def __init__(self,path):
        super(Player, self).__init__()
        self.surf = pygame.image.load(path).convert_alpha()
        self.rect = self.surf.get_rect()

class Boss(pygame.sprite.Sprite):
    def __init__(self):
        super(Boss, self).__init__()
        self.surf = pygame.Surface((20, 10))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()

class Ground(pygame.sprite.Sprite):
    def __init__(self):
        super(Ground, self).__init__()
        self.surf = pygame.image.load("ground.png").convert_alpha()
        self.rect = self.surf.get_rect()

class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super(Cloud, self).__init__()
        self.surf = pygame.image.load("cloud.png").convert_alpha()
        self.rect = self.surf.get_rect()

class Enemy(pygame.sprite.Sprite):
    def __init__(self,path):
        super(Enemy, self).__init__()
        self.surf = pygame.image.load(path).convert_alpha()
        self.rect = self.surf.get_rect()

def list1(x):
    j = 1
    c = []
    for i in range(1000000):
        j = j + x
        c.append(j)
    return(c)

def main_game():
    pygame.init()
    anim1 = list1(4)
    anim2 = list1(5)
    anim3 = list1(6)
    anim4 = list1(7)
    #print(list1(4))
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    X = SCREEN_WIDTH/2
    Y = 0
    RANDOM_OBJ = randint(1,5)
    Groundx = 0
    Groundx2 = 0
    cloud1 = 0
    cloud2 = 0
    cloud3 = 0
    tree = Enemy("tree.png")
    player = Player("dino.png")
    boss = Boss()
    ground = Ground()
    cloud = Cloud()
    running = True
    speed = 1
    s = 0
    time = 0
    enemy_speed = 0
    jump = 0
    nojump = 0
    ded = [270,271,272,273,274,275,276,277,278]
    jump_fix = [430,431,432,433,434,435,436,437,438,439]
    GAME_FONT = pygame.freetype.Font("arcade.ttf", 24)
    while running:
        enemy_speed = enemy_speed + speed
        s = s + 1
        if s % 6 == 0:
            time = time + 1
        if s % 100 == 0:
            speed = speed + 0.5
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                running = False
        pressed_keys = pygame.key.get_pressed()
        if s % 4 == 0 and not pressed_keys[K_DOWN]:
            player = Player("dino3.png")
        if s % 4 != 0 and not pressed_keys[K_DOWN]:
            player = Player("dino4.png")
        if pressed_keys[K_SPACE]:
            Y = 0
        if pressed_keys[K_DOWN] and s % 4 == 0:
            player = Player("dino5.png")            
        if pressed_keys[K_DOWN] and s % 4 != 0:
            player = Player("dino6.png")
        Groundx = Groundx + speed
        cloud1 = cloud1 + 1
        cloud2 = cloud2 + 1
        cloud3 = cloud3 + 1
        #screen.fill((255, 255, 255))
        screen.fill((255, 255, 255))
        screen.blit(cloud.surf, (70 - cloud1,30))
        screen.blit(cloud.surf, (970 - cloud2,40))
        screen.blit(cloud.surf, (570 - cloud3,70))
        screen.blit(cloud.surf, (1270 - cloud1,30))
        screen.blit(cloud.surf, (1770 - cloud2,40))
        screen.blit(cloud.surf, (1570 - cloud3,70))
        screen.blit(ground.surf, (0 - Groundx,400))
        screen.blit(ground.surf, (1200 - Groundx,400))
        dino_dead = 430 + Y + jump
        dino_pos = 430 + Y + jump
        if pressed_keys[K_DOWN]:
            screen.blit(player.surf, (189,430 + 35 + Y))
        if not pressed_keys[K_DOWN]:
            screen.blit(player.surf, (189,dino_dead))
        screen.blit(tree.surf, (1200 - speed - enemy_speed,430))
        if Groundx >= 1200:
            Groundx = 0
        if cloud1 >= 1200:
            cloud1 = 0
        if cloud2 >= 1200:
            cloud2 = 0
        if cloud3 >= 1200:
            cloud3 = 0
        if enemy_speed >= 1251:
            enemy_speed = 0
        
        if pressed_keys[K_SPACE] and dino_pos < 430:
            print("tu triche zeubi")
        if pressed_keys[K_SPACE]:
            if jump > -200:
                jump = jump - 10
            nojump = 19
        if not pressed_keys[K_SPACE]:
                if nojump > 1:
                    nojump = nojump - 0.75
                if jump < 1:
                    jump = jump + nojump + 1
        if int(dino_dead) != 430:
            dino_dead = 430
        if int(1200 - speed - enemy_speed) in ded and dino_dead < 450 and dino_dead > 334:
            quit()
        GAME_FONT.render_to(screen, (0, 0), "SCORE " + str(time), (83, 83, 83))
        pygame.display.flip()
        #print(nojump,jump)
        clock.tick(30)
main_game()