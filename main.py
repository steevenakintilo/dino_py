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
from os import system
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

def write_id(path,x):  
    f = open(path, "w")
    f.write(str(x))    
    f.close            

def print_file(path):
    f = open(path, 'r')
    content = f.read()
    return(content)
    f.close()

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

class Bird(pygame.sprite.Sprite):
    def __init__(self,path):
        super(Bird, self).__init__()
        self.surf = pygame.image.load(path).convert_alpha()
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

def make_list(x):
    x = x - 15
    de = 265
    ded = []
    k = de - x
    while de > k:
        ded.append(de)
        de = de - 1
    return (ded)

def time_list():
    l = 0
    c = []
    for i in range(10000):
        l = l + 98
        c.append(l)
    return (c)
def end_loop(SCORE,HIGHSCORE,x):
    pygame.mixer.Channel(1).play(pygame.mixer.Sound('death.ogg'))
    SCREEN_WIDTH = 1200
    SCREEN_HEIGHT = 600

    pygame.init()
    pygame.mixer.init()
    GAME_FONT = pygame.freetype.Font("arcade.ttf", 44)
    #pygame.mixer.Channel(0).play(pygame.mixer.Sound('music.ogg'),999)
    #pygame.mixer.Channel(1).play(pygame.mixer.Sound('boom.ogg'))

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    X = 100
    Y = SCREEN_HEIGHT/2

    clock = pygame.time.Clock()
    SPEED = 2.5
    #ADDENEMY = pygame.USEREVENT + 1
    #pygame.time.set_timer(ADDENEMY, 25)
    high = print_file("highscore.txt")

    player = Player("dino.png")
    end = 0
    #enemies = pygame.sprite.Group()
    #all_sprites = pygame.sprite.Group()
    #all_sprites.add(player)

    PASS = 0
    # Variable to keep the main loop running
    running = True

    # Main loop
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                quit()
        a = 0
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[ord('r')]:
            main_game()
            a = 1
        screen.fill((255, 255, 255))
        screen.blit(player.surf, (480,300))
        if x == 2:
            GAME_FONT.render_to(screen, (360, 430), "DONT USE SEVERAL KEYS AT ONCE", (83,83,83))
        GAME_FONT.render_to(screen, (460, 30), "GAME OVER", (83,83,83))
        GAME_FONT.render_to(screen, (370, 130), "SCORE " + str(SCORE), (83,83,83))
        GAME_FONT.render_to(screen, (370, 230), "HIGHSCORE " + str(HIGHSCORE), (83,83,83))
        GAME_FONT.render_to(screen, (370, 530), "PRESS R TO RESTART", (83,83,83))
        #GAME_FONT.render_to(screen, (0, 20), "HIGHSCORE: " + str(high), (255, 255, 255))

        pygame.display.flip()
        clock.tick(30)

def main_game():
    sound_jump = 0
    color = (83,83,83)
    system("clear")
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    X = SCREEN_WIDTH/2
    Y = 0
    RANDOM_OBJ = randint(1,6)
    Groundx = 0
    Groundx2 = 0
    cloud1 = 0
    cloud2 = 0
    cloud3 = 0
    high = print_file("highscore.txt")
    player = Player("dino.png")
    bird = Bird("bird.png")
    ground = Ground()
    cloud = Cloud()
    running = True
    speed = 10
    enemy_rdm = 0
    s = 0
    bird_pos = 0
    time = 0
    enemy_speed = 0
    enemy_speed2 = 0
    jump = 0
    nojump = 0
    enemy_distance = 0
    rdm_enemy = randint(1,6)
    rdm_enemy2 = randint(1,6)
    fly = 220
    #ded = [270,271,272,273,274,275,276,277,278]
    jump_fix = [430,431,432,433,434,435,436,437,438,439]
    GAME_FONT = pygame.freetype.Font("arcade.ttf", 24)
    BIGGAME_FONT = pygame.freetype.Font("arcade.ttf", 64)
    while running:
        #rdm_enemy = 1
        #rdm_enemy2 = 1
        bird_ded = make_list(92)
        if rdm_enemy == 1:
            tree = Enemy("tree.png")
            ded = make_list(50)
        if rdm_enemy2 == 1:
            tree2 = Enemy("tree.png")
            ded2 = make_list(50)
        if rdm_enemy == 2:
            tree = Enemy("3little_tree.png")
            ded = make_list(102)
        if rdm_enemy2 == 2:
            tree2 = Enemy("3little_tree.png")
            ded2 = make_list(102)
        if rdm_enemy == 3:
            tree = Enemy("2little_tree.png")
            ded = make_list(68)
        if rdm_enemy2 == 3:
            tree2 = Enemy("2little_tree.png")
            ded2 = make_list(68)
        if rdm_enemy == 4:
            tree = Enemy("1little_tree.png")
            ded = make_list(34)
        if rdm_enemy2 == 4:
            tree2 = Enemy("1little_tree.png")
            ded2 = make_list(34)
        if rdm_enemy == 5:
            tree = Enemy("4tree.png")
            ded = make_list(150)
        if rdm_enemy2 == 5:
            tree2 = Enemy("4tree.png")
            ded2 = make_list(150)
        if rdm_enemy == 6:
            tree = Enemy("2tree.png")
            ded = make_list(100)
        if rdm_enemy2 == 6:
            tree2 = Enemy("2tree.png")
            ded2 = make_list(100)
        enemy_speed = enemy_speed + speed
        enemy_speed2 = enemy_speed2 + speed
        if time > 250:
            bird_pos = bird_pos + 1.25 * speed
        s = s + 1
        #print(time_list())
        if s % 6 == 0:
            time = time + 1
        if time in time_list():
            pygame.mixer.Channel(1).play(pygame.mixer.Sound('up.ogg'))
        if s % 100 == 0:
            speed = speed + 0.5
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                running = False
        pressed_keys = pygame.key.get_pressed()
        if s % 4 == 0 and not pressed_keys[K_DOWN] and not pressed_keys[K_SPACE]:
            player = Player("dino3.png")
        if s % 4 != 0 and not pressed_keys[K_DOWN] and not pressed_keys[K_SPACE]:
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
        if pressed_keys[K_SPACE]:
            sound_jump = sound_jump + 1
        if not pressed_keys[K_SPACE]:
            sound_jump = 0
        if sound_jump == 1:
            pygame.mixer.Channel(1).play(pygame.mixer.Sound('jump.ogg'))
        if pressed_keys[K_DOWN] and pressed_keys[K_SPACE]:
            end_loop(time,high,2)
        if pressed_keys[K_DOWN] and not pressed_keys[K_SPACE]:
            screen.blit(player.surf, (189,430 + 35 + Y))
        if not pressed_keys[K_DOWN]:
            screen.blit(player.surf, (189,dino_dead))
        if s % 7 == 0:
            bird = Bird("bird.png")
        if s % 7 != 0:
            bird = Bird("bird2.png")
        if time > 250:
            screen.blit(bird.surf, (1200 - bird_pos,400))
        if rdm_enemy == 1:
            screen.blit(tree.surf, (1200 - speed - enemy_speed,430))
        if rdm_enemy == 2:
            screen.blit(tree.surf, (1200 - speed - enemy_speed,430+26))
        if rdm_enemy == 3:
            screen.blit(tree.surf, (1200 - speed - enemy_speed,430+26))
        if rdm_enemy == 4:
            screen.blit(tree.surf, (1200 - speed - enemy_speed,430+26))
        if rdm_enemy == 5:
            screen.blit(tree.surf, (1200 - speed - enemy_speed,430-2))
        if rdm_enemy == 6:
            screen.blit(tree.surf, (1200 - speed - enemy_speed,430))
        if rdm_enemy2 == 1:
            screen.blit(tree2.surf, (1600 + enemy_rdm - speed - enemy_speed2,430))
        if rdm_enemy2 == 2:
            screen.blit(tree2.surf, (1600 + enemy_rdm - speed - enemy_speed2,430+26))
        if rdm_enemy2 == 3:
            screen.blit(tree2.surf, (1600 + enemy_rdm - speed - enemy_speed2,430+26))
        if rdm_enemy2 == 4:
            screen.blit(tree2.surf, (1600 + enemy_rdm - speed - enemy_speed2,430+26))
        if rdm_enemy2 == 5:
            screen.blit(tree2.surf, (1600 + enemy_rdm - speed - enemy_speed2,430-2))
        if rdm_enemy2 == 6:
            screen.blit(tree2.surf, (1600 + enemy_rdm - speed - enemy_speed2,430))
        if Groundx >= 1200:
            Groundx = 0
        if cloud1 >= 1200:
            cloud1 = 0
        if cloud2 >= 1200:
            cloud2 = 0
        if cloud3 >= 1200:
            cloud3 = 0
        if time > 250:
            if bird_pos >= 1291:
                bird_pos = -5000
        if enemy_speed >= 1251:
            enemy_speed = - 400 - enemy_distance
            rdm_enemy = randint(1,6)
            #enemy_speed = 0
        elif enemy_speed2 >= 1651 + enemy_distance + enemy_rdm:
            enemy_speed2 = 0
            enemy_distance = randint(0,0)
            enemy_rdm = randint(200,700)
            rdm_enemy2 = randint(1,6)
        if pressed_keys[K_SPACE] and fly > 0:
            if fly > 0:
                fly = fly - 5
            if jump > -200:
                jump = jump - 10
            nojump = 19
        if not pressed_keys[K_SPACE]: 
                if fly < 220:
                    fly = fly + 5
                if nojump > 1:
                    nojump = nojump - 0.75
                if jump < 1:
                    jump = jump + nojump + 1
        if fly <= 0:
            fly = 0
            end_loop(time,high,1)
            #dino_dead = 430
        if int(dino_dead) != 430:
            dino_dead = 430
        if time > int(high):
            write_id("highscore.txt",time)
            high = print_file("highscore.txt")
        if time > 250:
            if int(1200 - bird_pos) in bird_ded and dino_pos < 400 and dino_pos > 332:
                      end_loop(time,high,1)
      
        if int(1200 - speed - enemy_speed) in ded and dino_pos < 450 and dino_pos > 354 and rdm_enemy == 1:
                  end_loop(time,high,1)
      
        if int(1600 + enemy_rdm - speed - enemy_speed2) in ded2 and dino_pos < 450 and dino_pos > 354 and rdm_enemy == 1:
                  end_loop(time,high,1)
      
        if int(1200 - speed - enemy_speed) in ded and dino_pos < 450 and dino_pos > 380 and rdm_enemy == 2:
                  end_loop(time,high,1)
      
        if int(1600 + enemy_rdm - speed - enemy_speed2) in ded2 and dino_pos < 450 and dino_pos > 380 and rdm_enemy == 2:
                  end_loop(time,high,1)
      
        if int(1200 - speed - enemy_speed) in ded and dino_pos < 450 and dino_pos > 380 and rdm_enemy == 3:
                  end_loop(time,high,1)
      
        if int(1600 + enemy_rdm - speed - enemy_speed2) in ded2 and dino_pos < 450 and dino_pos > 380 and rdm_enemy == 3:
                  end_loop(time,high,1)
      
        if int(1200 - speed - enemy_speed) in ded and dino_pos < 450 and dino_pos > 380 and rdm_enemy == 4:
                  end_loop(time,high,1)
      
        if int(1600 + enemy_rdm - speed - enemy_speed2) in ded2 and dino_pos < 450 and dino_pos > 380 and rdm_enemy == 4:
                  end_loop(time,high,1)
      
        if int(1200 - speed - enemy_speed) in ded and dino_pos < 450 and dino_pos > 352 and rdm_enemy == 5:
                  end_loop(time,high,1)
      
        if int(1600 + enemy_rdm - speed - enemy_speed2) in ded2 and dino_pos < 450 and dino_pos > 352 and rdm_enemy == 5:
                  end_loop(time,high,1)
      
        if int(1200 - speed - enemy_speed) in ded and dino_pos < 450 and dino_pos > 354 and rdm_enemy == 6:
                  end_loop(time,high,1)
      
        if int(1600 + enemy_rdm - speed - enemy_speed2) in ded2 and dino_pos < 450 and dino_pos > 354 and rdm_enemy == 6:
                  end_loop(time,high,1)
      
        GAME_FONT.render_to(screen, (0, 0), "SCORE " + str(time), (83, 83, 83))
        GAME_FONT.render_to(screen, (0, 20), "HIGHSCORE " + str(high), (83, 83, 83))
        #BIGGAME_FONT.render_to(screen, (480, 0), "ENERGY BAR", (83, 83, 83))
        BIGGAME_FONT.render_to(screen, (420, 0), "ENERGY BAR", (83, 83, 83))
        pygame.draw.rect(screen, color, pygame.Rect(472, 40, 220, 60),  2)
        pygame.draw.rect(screen, color, pygame.Rect(472, 40, fly, 60))
        pygame.display.flip()
        #print(dino_pos,1200 - speed - enemy_speed)
        #print(430+26,dino_pos)
        clock.tick(30)
main_game()