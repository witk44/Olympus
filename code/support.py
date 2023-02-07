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
def import_folder(path):
    surface_list = []
    for _,__,image_files in walk(path):
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
# print(import_csv_layout('data\levels\level0\INTRO._Obstacles.csv'))
