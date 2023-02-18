import pygame
from settings import *

class Upgrade():
    def __init__(self,player):

        self.display_surface = pygame.display.get_surface()
        self.player = player
        self.attribute_nr = len(player.stats)
        self.attribute_names = list(player.stats.keys())
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)

        #selection system
        self.selection_index = 0
        self.selection_time = None
        self.can_move = True

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and self.can_move:
            self.selection_index +=1
            self.can_move = False
            self.selection_time = pygame.time.get_ticks()
        elif keys[pygame.K_LEFT] and self.can_move:
            self.selection_index -=1
            self.can_move = False
            self.selection_time = pygame.time.get_ticks()

        if keys[pygame.K_SPACE]:
            pass

    def selection_cooldown(self):
        if not self.can_move:
            current_time = pygame.time.get_ticks()
            if current_time - self.selection_time >= 250:
                self.can_move = True

    def display(self):
        self.input()
        self.selection_cooldown()
