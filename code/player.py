import pygame,sys
import json
import os
from settings import *
from pygame.locals import *
from support import *
from entity import Entity

class Player(Entity):
    def __init__(self,pos,groups,obstacle_sprites,attackable_sprites,create_attack,destroy_attack,create_magic):
        super().__init__(groups)
        pygame.init()
        
        if os.path.exists("../save_files/player.json"):
            saved_player_file = open("../save_files/player.json")
            saved_player = json.load(saved_player_file)
            self.sprite_type = saved_player["sprite_type"]
            self.image = pygame.image.load('../graphics/player/' + self.sprite_type + '.png').convert_alpha()
            self.rect = self.image.get_rect(topleft = (saved_player["x"],saved_player["y"]))
            
            self.hitbox = self.rect.inflate(0,HITBOX_OFFSET['player'])
            self.import_player_assets()
            self.status = saved_player["status"]
            self.alive = True
            self.escape_key = False
            self.last_key_pressed = None
            self.attacking = False
            self.attack_cooldown = 300
            self.attack_time = None
            self.obstacle_sprites = obstacle_sprites
            self.attackable_sprites = attackable_sprites
            

            #weapon
            self.create_attack = create_attack
            self.can_switch_weapon = True
            self.weapon_switch_time = None
            self.switch_duration_cooldown = 200
            self.destroy_attack = destroy_attack
            self.weapon_index = saved_player['weapon_index']
            self.weapon = list(weapon_data.keys())[self.weapon_index]

            #magic
            self.create_magic = create_magic
            self.magic_index = saved_player['magic_index']
            self.magic = list(magic_data.keys())[self.magic_index]

            self.can_switch_magic = True
            self.magic_switch_time = None


            #stats
            self.stats = saved_player['stats']
            self.max_stats = {"health": 400, "energy": 200, "attack": 100, "magic":100, "speed": 9}
            self.upgrade_cost = saved_player['upgrade_cost']
            self.health = saved_player['health']
            self.energy = saved_player['energy']
            self.spell_dmg  = self.stats['magic']
            self.exp = saved_player['exp']
            self.speed = saved_player['speed']
            self.magic = saved_player['magic']
                    
            #damge timer
            self.hittable = True
            self.hurt_time = None
            self.invulnerability_duration = 600

            self.weapon_attack_sound = pygame.mixer.Sound('../audio/sword.wav')
            self.weapon_attack_sound.set_volume(0.3)
        else:
            self.sprite_type = 'player'
            self.image = pygame.image.load('../graphics/player/player.png').convert_alpha()
            self.rect = self.image.get_rect(topleft = pos)
            
            self.hitbox = self.rect.inflate(0,HITBOX_OFFSET['player'])
            self.import_player_assets()
            self.status = 'down'
            self.alive = True
            self.escape_key = False
            self.last_key_pressed = None
            self.attacking = False
            self.attack_cooldown = 300
            self.attack_time = None
            self.obstacle_sprites = obstacle_sprites
            self.attackable_sprites = attackable_sprites
            

            #weapon
            self.create_attack = create_attack
            self.can_switch_weapon = True
            self.weapon_switch_time = None
            self.switch_duration_cooldown = 200
            self.destroy_attack = destroy_attack
            self.weapon_index = 0
            self.weapon = list(weapon_data.keys())[self.weapon_index]

            #magic
            self.create_magic = create_magic
            self.magic_index = 0
            self.magic = list(magic_data.keys())[self.magic_index]

            self.can_switch_magic = True
            self.magic_switch_time = None


            #stats
            self.stats = {"health": 100, "energy": 60, "attack": 10, "magic":4, "speed": 4}
            self.max_stats = {"health": 400, "energy": 200, "attack": 100, "magic":100, "speed": 9}
            self.upgrade_cost = {"health": 100, "energy": 100, "attack": 100, "magic":100, "speed": 100}
            self.health = self.stats['health']
            self.energy = self.stats['energy']
            self.spell_dmg  = self.stats['magic']
            self.exp = 0
            self.speed = self.stats['speed']
                    
            #damge timer
            self.hittable = True
            self.hurt_time = None
            self.invulnerability_duration = 600

            self.weapon_attack_sound = pygame.mixer.Sound('../audio/sword.wav')
            self.weapon_attack_sound.set_volume(0.3)
        

       
    def import_player_assets(self):
        character_path = '../graphics/player/'
        self.animations = {'up': [],'down': [],'left': [],'right': [],'right_idle': [],
                            'left_idle': [],'up_idle': [],'down_idle': [],'right_attack': [],
                            'left_attack': [],'up_attack': [],'down_attack': [],}
        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)

    def input(self):
        if not self.attacking:
            keys = pygame.key.get_pressed()  
            if keys[pygame.K_ESCAPE] :
                s = self.serialize()
                out_file = open("../save_files/player.json", "w")
                json.dump(s,out_file,indent=6)
                out_file.close()
                self.kill()
                self.escape_key = True
            if keys[pygame.K_UP] or keys[pygame.K_w]:
                self.direction.y = -1
                self.status = 'up'
            elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
                self.direction.y = 1
                self.status = 'down'
            else:
                self.direction.y = 0
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                self.direction.x = -1
                self.status = 'left'
                
            elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                self.direction.x = 1
                self.status = 'right'
                
            else:
                self.direction.x = 0
            
            left, middle, right = pygame.mouse.get_pressed()
            #attack input
            if  left and not self.attacking:
                self.attacking = True
                self.attack_time = pygame.time.get_ticks()
                self.create_attack()
                self.weapon_attack_sound.play()
            elif  right and not self.attacking:
                self.attacking = True
                self.attack_time = pygame.time.get_ticks()
                style = list(magic_data.keys())[self.magic_index]
                strength = list(magic_data.values())[self.magic_index]["strength"] + self.spell_dmg
                cost = list(magic_data.values())[self.magic_index]["cost"]
                self.create_magic(style,strength,cost)

            if keys[K_LSHIFT] and self.can_switch_weapon:
                self.can_switch_weapon = False
                self.weapon_switch_time = pygame.time.get_ticks()
                
                if self.weapon_index < len(list(weapon_data.keys())) - 1:
                    self.weapon_index += 1
                else:
                    self.weapon_index = 0
                self.weapon = list(weapon_data.keys())[self.weapon_index]
            elif keys[K_RSHIFT] and self.can_switch_magic:
                self.can_switch_magic = False
                self.magic_switch_time = pygame.time.get_ticks()
                
                if self.magic_index < len(list(magic_data.keys())) - 1:
                    self.magic_index += 1
                else:
                    self.magic_index = 0
                self.magic = list(magic_data.keys())[self.magic_index]
            
    def get_status(self):
        if self.direction.x == 0 and self.direction.y == 0:
            if not 'idle' in self.status and not 'attack' in self.status:
                self.status = self.status + '_idle'
            else:
                self.status = self.status.replace('_attack','_idle')

        if self.attacking:
            self.direction.x = 0
            self.direction.y = 0
            if not 'attack' in self.status and not 'idle' in self.status:
                self.status = self.status + '_attack'
            else:
                self.status = self.status.replace('_idle','_attack')
        else:
            if 'attack' in self.status:
                self.status = self.status('_attack', '')

    def get_weapon_damage(self):
        base_damage = self.stats['attack']
        weapon_damage = weapon_data[self.weapon]['damage']
        return base_damage + weapon_damage

    def get_magic_damage(self):
        base_damge = self.spell_dmg
        spell_damage = magic_data[self.magic]['strength'] 
        return base_damge + spell_damage

    def animate(self):
        animation = self.animations[self.status]
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0
        
        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center = self.hitbox.center)

        if not self.hittable:
            alpha = self.wave_value()
            self.image.set_alpha(alpha)
        else:
            self.image.set_alpha(255)

    def cooldowns(self):
        current_time = pygame.time.get_ticks()
        if self.attacking:
            if current_time - self.attack_time >= self.attack_cooldown :
                self.attacking = False
                self.destroy_attack()
        elif not self.can_switch_weapon:
            if current_time - self.weapon_switch_time >= self.switch_duration_cooldown:
                self.can_switch_weapon = True
        elif not self.can_switch_magic:
            if current_time - self.magic_switch_time >= self.switch_duration_cooldown:
                self.can_switch_magic = True
        if not self.hittable:
            if current_time - self.hurt_time >= self.invulnerability_duration:
                self.hittable = True

    def get_value_by_index(self,index):
        return list(self.stats.values())[index]


    def get_cost_by_index(self,index):
        return list(self.upgrade_cost.values())[index]

    def energy_recovery(self):
        if self.energy < self.stats['energy']:
            self.energy += .01 * self.stats['magic']
        else:
            self.energy = self.stats['energy']
                
    def upgrade_current_attribute(self,upgrade_attribute):
        if upgrade_attribute == 'health':
            self.health = self.stats[upgrade_attribute]
            
        elif upgrade_attribute == 'magic':
            self.spell_dmg = self.stats[upgrade_attribute]
            
        elif upgrade_attribute == 'attack':
            self.attack = self.stats[upgrade_attribute]
        elif upgrade_attribute == 'speed':
            self.speed = self.stats[upgrade_attribute]
        elif upgrade_attribute == 'energy':
            self.energy = self.stats[upgrade_attribute]
    def update(self):
        self.input()
        self.cooldowns()
        self.get_status()
        self.animate()
        self.move(self.speed)
        self.energy_recovery()
    
    def serialize(self):
        self.x = int(self.rect.x)
        self.y= int(self.rect.y)
       
        return {"sprite_type": self.sprite_type,
                    'image': self.sprite_type + '.png',
                    'status': self.status,
                    'x':    self.x,
                    'y': self.y,
                    'weapon_index': self.weapon_index,
                    'magic_index': self.magic_index,
                    'stats': self.stats,
                    'upgrade_cost': self.upgrade_cost,
                    'health': self.health,
                    'energy': self.energy,
                    'magic': self.magic,
                    'exp':self.exp,
                    'speed':self.speed
                    }