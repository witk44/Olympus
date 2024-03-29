import pygame
from resources.code.settings import *
from random import randint


class MagicPlayer:
    def __init__(self,animation_player):
        self.animation_player = animation_player
        self.sounds = {
            'heal': pygame.mixer.Sound(app_path('resources/audio/heal.wav')),
            'lightning': pygame.mixer.Sound(app_path('resources/audio/Fire.wav'))
        }
    def heal(self,player,strength,cost,groups):
        if player.energy >= cost and player.health != player.stats['health']:
            self.sounds['heal'].set_volume(0.3)
            self.sounds['heal'].play()
            if player.health + strength >= player.stats['health']:
                player.health = player.stats['health']
                player.energy -= cost
                self.animation_player.create_particles('heal',player.rect.center,groups)
            else:
                player.energy -= cost
                player.health += strength
                self.animation_player.create_particles('heal',player.rect.center,groups)
            
    def lightning(self,player,cost,groups):
        if player.energy >= cost:
            player.energy-=cost
            self.sounds['lightning'].set_volume(0.3)
            self.sounds['lightning'].play()
            if player.status.split('_')[0] == 'right': direction = pygame.math.Vector2(1,0)
            elif player.status.split('_')[0] == 'left': direction = pygame.math.Vector2(-1,0)
            elif player.status.split('_')[0] == 'up': direction = pygame.math.Vector2(0,-1)
            elif player.status.split('_')[0] == 'down': direction = pygame.math.Vector2(0,1)

            for i in range(1,6):
                if direction.x:
                    offset_x = (direction.x * i)*TILESIZE
                    x = player.rect.centerx + offset_x + randint(-TILESIZE // 6,TILESIZE // 6)
                    y  = player.rect.centery + randint(-TILESIZE // 6,TILESIZE // 6)
                    if i == 1: x = player.rect.centerx + offset_x
                    self.animation_player.create_particles('lightning',(x,y),groups)
                else:
                    offset_y = (direction.y * i)*TILESIZE
                    x = player.rect.centerx +  randint(-TILESIZE // 6,TILESIZE // 6)
                    y  = player.rect.centery + offset_y + randint(-TILESIZE // 6,TILESIZE // 6)
                    if i == 1: y = player.rect.centery + offset_y
                    self.animation_player.create_particles('lightning',(x,y),groups)