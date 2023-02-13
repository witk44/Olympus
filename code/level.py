import pygame
from settings import *
from tile import Tile
from player import Player
from debug import debug
from support import *
from weapon import Weapon
from UI import UI
from enemy import Enemy
class Level:
    def __init__(self) -> None:
        # get the display surface
        self.display_surface = pygame.display.get_surface()
        # sprite group setup
        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()

        #attack sprites
        self.current_attack = None

        #sprite setup
        self.create_map()

        #ui
        self.ui = UI()

        

    def create_map(self):
        layouts = {
            'boundary': import_csv_layout('data/levels/level0/INTRO._FloorBlocks.csv'),
            'obstacles': import_csv_layout('data\levels\level0\INTRO._Obstacles.csv'),
            'old_tree': import_csv_layout('data\levels\level0\INTRO._Tree.csv'),
            'entities': import_csv_layout('data\levels\level0\INTRO._Enemy.csv'),
            'player': import_csv_layout('data\levels\level0\INTRO._Player.csv')
        }
        graphics = {
            'tileset':import_folder('graphics/tileset',True),
            # 'tutorial':import_folder('graphics/tutorial')
        }
        for style,layout in layouts.items():
            for row_index,row in enumerate(layout):
                for col_index,col in enumerate(row):
                    if col != '-1':
                        x = col_index*TILESIZE
                        y = row_index*TILESIZE
                        if style == 'boundary':
                            Tile((x,y),[self.obstacle_sprites],'invisible')
                        #draw obstacles on map that are visible and colidable (this is where draw error is happening)
                        elif style == 'obstacles':                                         
                            surf = graphics['tileset'][int(col)]
                            Tile((x,y),[self.visible_sprites,self.obstacle_sprites],'obstacles',surf)
                        elif style == 'old_tree':                                         
                            surf = graphics['tileset'][int(col)]
                            Tile((x,y),[self.visible_sprites],'old_tree',surf)
                        elif style == 'entities':
                            if col == '0':
                                Enemy('bamboo',(x,y),[self.visible_sprites])
                        elif style == 'player':
                            if col == '0':
                                self.player = Player((x,y),[self.visible_sprites],self.obstacle_sprites,self.create_attack,self.destroy_attack, self.create_magic)
            

    def destroy_attack(self):
        if self.current_attack:
            self.current_attack.kill()
        self.current_attack = None

    def create_attack(self):
        self.current_attack = Weapon(self.player,[self.visible_sprites])

    def create_magic(self,style,strength,cost):
        print(style)
        print(strength)
        print(cost)

    def run(self):
        #update and draw game
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        debug(self.player.status)
        self.ui.display(self.player)


class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2

        self.offset = pygame.math.Vector2(100,200)


    def custom_draw(self,player):
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height
        #creating the floor
        self.floor_surface = pygame.image.load('data\levels\level0\INTRO.png').convert()
        self.floor_rect = self.floor_surface.get_rect(topleft = (0,0))
        #drawing the floor
        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surface,floor_offset_pos)
        #draws all elements
        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offset_position = sprite.rect.topleft-self.offset
            self.display_surface.blit(sprite.image,offset_position)
