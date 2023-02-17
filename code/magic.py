import pygame
from settings import *

class MagicPlayer:
    def __init__(self,animation_player):
        self.animation_player = animation_player

    def heal(self,player,strength,cost,groups):
        if player.energy >= cost and player.health != player.stats['health']:
            if player.health + strength >= player.stats['health']:
                player.health = player.stats['health']
                player.energy -= cost
            else:
                player.energy -= cost
                player.health += strength
                self.animation_player.create_particles('heal',player.rect.center,groups)
        print('heal')
    def lightning(self):
        pass