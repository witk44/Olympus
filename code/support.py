from csv import reader
from os import walk
import pygame
def import_csv_layout(path):
    terrain_map = []
    with open(path) as level_map:
        layout = reader(level_map,delimiter=',')
        for row in layout:
            terrain_map.append(list(row))
        return terrain_map
def import_folder(path,sort = False):
    surface_list = []
    for _,__,image_files in walk(path):
        if sort:
            image_files = custom_sort(image_files)
        for image in image_files:
            full_path = path + "/" + image
            image_surface = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surface)
        
    # surface_list.sort()
    return surface_list

def custom_sort(images):
    for index,image in enumerate(images):
        if(index < 10):
            images[index] = '00' + str(index) + '.png'
        elif(index < 100):
            images[index] = '0' + str(index) + '.png'
        else:
            images[index] = str(index) + '.png' 
            
    return images

def create_animation(action,direction = None):
        if(action == "walking"):
            if(direction == "up"):
                walking_up = []
                int = 1
                while(int<65):
                    if (int<17):
                        walking_up.append(pygame.image.load('graphics/player/walking/tile001.png'))
                    elif(int<33):
                        walking_up.append(pygame.image.load('graphics/player/walking/tile005.png'))
                    elif(int<49):
                        walking_up.append(pygame.image.load('graphics/player/walking/tile009.png'))
                    else:
                        walking_up.append(pygame.image.load('graphics/player/walking/tile013.png'))
                    int+=1
                return walking_up
            elif(direction == "down"):
                walking_down = []
                int = 1
                while(int<65):
                    if (int<17):
                        walking_down.append(pygame.image.load('graphics/player/walking/tile000.png'))
                    elif(int<33):
                        walking_down.append(pygame.image.load('graphics/player/walking/tile004.png'))
                    elif(int<49):
                        walking_down.append(pygame.image.load('graphics/player/walking/tile008.png'))
                    else:
                        walking_down.append(pygame.image.load('graphics/player/walking/tile012.png'))
                    int+=1
                return walking_down
            elif(direction == "right"):
                walking_right = []
                int = 1
                while(int<65):
                    if (int<17):
                        walking_right.append(pygame.image.load('graphics/player/walking/tile003.png'))
                    elif(int<33):
                        walking_right.append(pygame.image.load('graphics/player/walking/tile007.png'))
                    elif(int<49):
                        walking_right.append(pygame.image.load('graphics/player/walking/tile011.png'))
                    else:
                        walking_right.append(pygame.image.load('graphics/player/walking/tile015.png'))
                    int+=1
                return walking_right
            else:
                walking_left = []
                int = 1
                while(int<65):
                    if (int<17):
                        walking_left.append(pygame.image.load('graphics/player/walking/tile002.png'))
                    elif(int<33):
                        walking_left.append(pygame.image.load('graphics/player/walking/tile006.png'))
                    elif(int<49):
                        walking_left.append(pygame.image.load('graphics/player/walking/tile010.png'))
                    else:
                        walking_left.append(pygame.image.load('graphics/player/walking/tile014.png'))
                    int+=1
                return walking_left
        elif(action == "idle"):
            idle = []
            idle.append(pygame.image.load('graphics/player/idle/tile000.png'))
            idle.append(pygame.image.load('graphics/player/idle/tile001.png'))
            idle.append(pygame.image.load('graphics/player/idle/tile002.png'))
            idle.append(pygame.image.load('graphics/player/idle/tile003.png'))
            return idle
# print(import_csv_layout('data\levels\level0\INTRO._Obstacles.csv'))
