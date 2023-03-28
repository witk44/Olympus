
import pygame,sys
import resources.code.level
from resources.code.settings import *

class MainMenu:
    def __init__(self):

        self.display_surface = pygame.display.get_surface()
        self.attribute_nr = 2
        self.attribute_names = ['New Game','Load Game']
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)

        #dimensionss
        self.height = self.display_surface.get_size()[1]*0.8 
        self.width = self.display_surface.get_size()[0]//6
        self.create_items()
        #selection system
        self.selection_index = 0
        self.selection_time = None
        self.can_move = True

    def input(self):
        keys = pygame.key.get_pressed()
        if  self.can_move:
            if (keys[pygame.K_UP] or keys[pygame.K_w]) and self.selection_index >=1:
                self.selection_index -=1
                self.can_move = False
                self.selection_time = pygame.time.get_ticks()
            elif (keys[pygame.K_DOWN] or keys[pygame.K_s]) and self.selection_index < self.attribute_nr - 1:
                self.selection_index +=1
                self.can_move = False
                self.selection_time = pygame.time.get_ticks()

            if keys[pygame.K_SPACE]:
                self.can_move = False
                self.selection_time = pygame.time.get_ticks()
                self.item_list[self.selection_index].trigger(self.selection_index)

    def selection_cooldown(self):
        if not self.can_move:
            current_time = pygame.time.get_ticks()
            if current_time - self.selection_time >= 200:
                self.can_move = True

    def create_items(self):
        self.item_list = []
        for item,index in enumerate(range(self.attribute_nr)):
            full_width = self.display_surface.get_size()[0]
            increment = full_width // (self.attribute_nr + 2)
            left = (item*increment)+(increment-self.width) // 2

            top = self.display_surface.get_size()[1]*.1

            item = Option(left,top,self.width,self.height,index,self.font)
            self.item_list.append(item)
        print(self.item_list)
    def display(self):
        self.input()
        self.selection_cooldown()
        for index, item in enumerate(self.item_list):
            #attributes
            name = self.attribute_names[index]
            item.display(self.display_surface,self.selection_index,name)

class Option:
    def __init__(self,l,t,w,h,index,font):
        self.rect = pygame.rect.Rect(l,t,w,h)
        self.index = index
        self.font = font
    
    def display_names(self,surface,name,selected):
        color = TEXT_COLOR_SELECTED if selected else TEXT_COLOR
        name = name.capitalize()
        title_surf = self.font.render(name,False,color)
        title_rect = title_surf.get_rect(midtop = self.rect.midtop + pygame.math.Vector2(0,20))


        surface.blit(title_surf,title_rect)

    def trigger(self,index):
        if index == 0:
            return True
        return False
    def display(self,surface,selection_num,name):
        if self.index == selection_num:
            pygame.draw.rect(surface,UPGRADE_BG_COLOR_SELECTED,self.rect)
            pygame.draw.rect(surface,UI_BORDER_COLOR,self.rect,4)
        else:
            pygame.draw.rect(surface,UI_BG_COLOR,self.rect)
            pygame.draw.rect(surface,UI_BORDER_COLOR,self.rect,4)
        self.display_names(surface,name,self.index == selection_num)