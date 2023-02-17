import pygame
from settings import *
from tile import Tile
from player import Player
from debug import debug
from support import *
from random import choice,randint
from weapon import Weapon
from UI import UI
from enemy import Enemy
from particles import AnimationPlayer
from magic import *

class Level:
    def __init__(self) -> None:
        # get the display surface
        self.display_surface = pygame.display.get_surface()
        # sprite group setup
        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()

        #attack sprites
        self.current_attack = None
        self.attack_sprites = pygame.sprite.Group()
        self.attackable_sprites = pygame.sprite.Group()

        #sprite setup
        self.create_map()

        #ui
        self.ui = UI()

        self.animation_player = AnimationPlayer()
        self.magic_player = MagicPlayer(self.animation_player)

    def create_map(self):
        layouts = {
            'boundary': import_csv_layout('../data/levels/level0/INTRO._FloorBlocks.csv'),
            'obstacles': import_csv_layout('../data\levels\level0\INTRO._Obstacles.csv'),
            'old_tree': import_csv_layout('../data\levels\level0\INTRO._Tree.csv'),
            'entities': import_csv_layout('../data\levels\level0\INTRO._Enemy.csv'),
            'player': import_csv_layout('../data\levels\level0\INTRO._Player.csv')
        }
        graphics = {
            'tileset':import_folder('../graphics/tileset',True),
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
                                monster_name = 'squid'
                                
                            elif col == '1':
                                monster_name = 'raccoon'
                                
                            elif col == '2':
                                monster_name = 'spirit'
                                
                            elif col == '3':
                                monster_name = 'bamboo'
                                
                            Enemy(monster_name,(x,y),[self.visible_sprites,
                                self.attackable_sprites],self.obstacle_sprites, self.damage_player, self.trigger_death_particles)
                        elif style == 'player':
                            if col == '0':
                                self.player = Player((x,y),[self.visible_sprites],
                                self.obstacle_sprites,self.create_attack,self.destroy_attack, self.create_magic)
            

    def destroy_attack(self):
        if self.current_attack:
            self.current_attack.kill()
        self.current_attack = None

    def player_attack_logic(self):
        if self.attack_sprites:
            for attack_sprite in self.attack_sprites:
                collision_sprites = pygame.sprite.spritecollide(attack_sprite,self.attackable_sprites,False)
                if collision_sprites:
                    for target_sprite in collision_sprites:
                        if target_sprite.sprite_type == 'grass':
                            pos = target_sprite.rect.center
                            offset = pygame.math.Vector2(0,55)
                            for leaf in range(randint(3,6)):

                                self.animation_player.create_grass_particles(pos-offset,[self.visible_sprites])
                            target_sprite.kill()
                        else:
                            target_sprite.get_damge(self.player,attack_sprite.sprite_type)
    def create_attack(self):
        self.current_attack = Weapon(self.player,[self.visible_sprites,self.attack_sprites])

    def create_magic(self,style,strength,cost):
        if style == 'heal':
            self.magic_player.heal(self.player,strength,cost,[self.visible_sprites])
        if style == 'lightning':
            self.magic_player.lightning(self.player,cost,[self.visible_sprites, self.attack_sprites])
        print(style)
        print(strength)
        print(cost)

    def damage_player(self,amount,attack_type):
        if self.player.hittable:
            self.player.health -= amount
            self.player.hittable = False
            self.player.hurt_time = pygame.time.get_ticks()
            self.animation_player.create_particles(attack_type,self.player.rect.center,[self.visible_sprites])
            
    def trigger_death_particles(self,pos,particle_type):
            self.animation_player.create_particles(particle_type,pos,[self.visible_sprites])


    def run(self):
        #update and draw game
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        self.visible_sprites.enemy_update(self.player)
        self.player_attack_logic()
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
        self.floor_surface = pygame.image.load('..\data\levels\level0\INTRO.png').convert()
        self.floor_rect = self.floor_surface.get_rect(topleft = (0,0))
        #drawing the floor
        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surface,floor_offset_pos)
        #draws all elements
        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offset_position = sprite.rect.topleft-self.offset
            self.display_surface.blit(sprite.image,offset_position)

    def enemy_update(self,player):
        enemy_sprites = [sprite for sprite in self.sprites() if hasattr(sprite,'sprite_type') and sprite.sprite_type == 'enemy']
        for enemy in enemy_sprites:
            enemy.enemy_update(player)