import pygame
from settings import *
from pygame.locals import *
from support import *


class Player(pygame.sprite.Sprite):
    def __init__(self,pos,groups,obstacle_sprites):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/player/player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-26)
        self.direction = pygame.math.Vector2()
        self.speed = 5
        self.obstacle_sprites = obstacle_sprites
        self.animation_index = 0
        self.walking_up = create_animation("walking","up") #[pygame.image.load('graphics/player/walking/tile001.png'),pygame.image.load('graphics/player/walking/tile001.png'),pygame.image.load('graphics/player/walking/tile001.png'),pygame.image.load('graphics/player/walking/tile001.png'),pygame.image.load('graphics/player/walking/tile005.png'),pygame.image.load('graphics/player/walking/tile005.png'),pygame.image.load('graphics/player/walking/tile005.png'),pygame.image.load('graphics/player/walking/tile005.png'),pygame.image.load('graphics/player/walking/tile005.png'),pygame.image.load('graphics/player/walking/tile009.png'),pygame.image.load('graphics/player/walking/tile009.png'),pygame.image.load('graphics/player/walking/tile009.png'),pygame.image.load('graphics/player/walking/tile009.png'),pygame.image.load('graphics/player/walking/tile009.png'),pygame.image.load('graphics/player/walking/tile009.png'),pygame.image.load('graphics/player/walking/tile009.png'),pygame.image.load('graphics/player/walking/tile013.png')]
        self.walking_down = create_animation("walking","down")
        self.walking_right = create_animation("walking","right")
        self.walking_left = create_animation("walking","left")
        self.idle = create_animation("idle")
        self.clock = pygame.time.Clock()
        self.facing = "S"
        self.attack_animations = [pygame.image.load('graphics/player/attacking/tile000.png'),pygame.image.load('graphics/player/attacking/tile001.png'),pygame.image.load('graphics/player/attacking/tile002.png'),pygame.image.load('graphics/player/attacking/tile003.png')]
    def input(self):
        keys = pygame.key.get_pressed()  
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
        if keys[pygame.K_UP] or keys[pygame.K_w]:

            if self.animation_index >= len(self.walking_up):
                self.animation_index = 0
            self.direction.y = -1
            # self.clock.tick(FPS)
            self.image = self.walking_up[self.animation_index]
            self.animation_index +=1
            self.facing = "N"
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            if self.animation_index >= len(self.walking_up):
                self.animation_index = 0
            self.direction.y = 1
            # self.clock.tick(FPS)
            self.image = self.walking_down[self.animation_index]
            self.animation_index +=1
            self.facing = "S"
        else:
            self.direction.y = 0
            if(self.facing == 'N'):
                self.image = self.idle[1]
            elif(self.facing == 'S'):
                self.image = self.idle[0]
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if self.animation_index >= len(self.walking_up):
                self.animation_index = 0
            self.direction.x = -1
            # if not (keys[pygame.K_UP] or keys[pygame.K_w] or keys[pygame.K_DOWN] or keys[pygame.K_s]):
                # self.clock.tick(FPS)
            self.image = self.walking_left[self.animation_index]
            self.animation_index +=1
            self.facing = "W"
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if self.animation_index >= len(self.walking_up):
                self.animation_index = 0
            self.direction.x = 1
            # if not (keys[pygame.K_UP] or keys[pygame.K_w] or keys[pygame.K_DOWN] or keys[pygame.K_s]):
                # self.clock.tick(FPS)
            self.image = self.walking_right[self.animation_index]
            self.animation_index +=1
            self.facing = "E"
        else:
            self.direction.x = 0
            if(self.facing == 'E'):
                self.image = self.idle[3]
            elif(self.facing == 'W'):
                self.image = self.idle[2]
        left, middle, right = pygame.mouse.get_pressed()
        #attack input
        if  left:
            if self.facing == "N":
                self.image = self.attack_animations[1]
            elif self.facing == "S":
                self.image = self.attack_animations[0]
            elif self.facing == "W":
                self.image = self.attack_animations[2]
            elif self.facing == "E":
                self.image = self.attack_animations[3]
                
            
        #special ability input

        
    def move(self,speed):
        if self.direction.magnitude() != 0:
            # accounts for diagnol movement so you do not move double speed diagonolly
            self.direction = self.direction.normalize()
        self.hitbox.x += self.direction.x*speed
        self.collision('horizontal')
        self.hitbox.y += self.direction.y*speed
        self.collision('vertical')
        self.rect.center = self.hitbox.center

    def collision(self,direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0: #moving right
                        self.hitbox.right = sprite.hitbox.left
                    elif self.direction.x < 0: #moving left
                        self.hitbox.left = sprite.hitbox.right
        elif direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0: #moving down
                        self.hitbox.bottom = sprite.hitbox.top
                    elif self.direction.y < 0: #moving up
                        self.hitbox.top = sprite.hitbox.bottom


    def update(self):
        self.input()
        self.move(self.speed)

    