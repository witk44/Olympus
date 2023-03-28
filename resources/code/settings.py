import pygame
import os,sys
screen = pygame.display.set_mode()
WIDTH, HEIGHT = screen.get_size()
def app_path(path):
    frozen = 'not'
    if getattr(sys, 'frozen', False):
            # we are running in executable mode
            frozen = 'ever so'
            app_dir = sys._MEIPASS
            return os.path.join(app_dir, path)
    else:
            # we are running in a normal Python environment
            return path
# WIDTH    = 1240
# HEIGHT   =  680  #800
FPS      = 90
TILESIZE = 64
HITBOX_OFFSET ={
    'player': -26,
    'obstacles': 0,
    'old_tree': 0,
    'grass':-10,
    'invisible':0
}
UPDATE_RADIUS = 700
BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 200
ENERGY_BAR_WIDTH = 140
ITEM_BOX_SIZE = 100
UI_FONT = app_path('resources/graphics/font/neon.ttf')
UI_FONT_SIZE = 16
BLOODY_FONT = app_path('resources/graphics/font/BloodytypepersonaluseBold-OVe6e.otf')
FLYING_BIRD_FONT = app_path('resources/graphics/font/FlyingBird-Yz9Ga.otf')
RICH_THE_BARBER_FONT = app_path('resources/graphics/font/RichTheBarberPersonalUse-gx824.ttf')

# general colors
WATER_COLOR = '#71ddee'
UI_BG_COLOR = '#222222'
UI_BORDER_COLOR = 'gray'
TEXT_COLOR = '#EEEEEE'
TEXT_COLOR_SELECTED = 'black'
 
# ui colors
HEALTH_COLOR = 'red'
ENERGY_COLOR = 'green'
UI_BORDER_COLOR_ACTIVE = 'gold'
UPGRADE_BG_COLOR_SELECTED = 'white'
BAR_COLOR = 'white'
BAR_COLOR_SELECTED = 'black'


    

weapon_data = {
    'sword': {'cooldown': 500, 'damage': 15,'graphic': app_path('resources/graphics/weapons/sword/full.png')},
    'bigsword': {'cooldown': 800, 'damage': 30,'graphic':app_path('resources/graphics/weapons/bigsword/full.png')},
    'axe': {'cooldown': 700, 'damage': 20, 'graphic':app_path('resources/graphics/weapons/axe/full.png')},
    'katana':{'cooldown': 450, 'damage': 8, 'graphic':app_path('resources/graphics/weapons/katana/full.png')},
    'lance':{'cooldown': 550, 'damage': 10, 'graphic':app_path('resources/graphics/weapons/lance/full.png')}}

magic_data = {
    'lightning': {'strength': 20,'cost': 20,'graphic':app_path('resources/graphics/particles/lightning_ball/tile000.png')},
    'heal' : {'strength': 10,'cost': 20,'graphic':app_path('resources/graphics/particles/heal/tile000.png')}}

monster_data = {
    'squid': {'health': 100,'exp':100,'damage':20,'attack_type': 'slash', 'attack_sound':app_path('resources/audio/attack/slash.wav'), 'speed': 3, 'resistance': 3, 'attack_radius': 69, 'notice_radius': 360, "update_radius":500},
    'cyclops': {'health': 75,'exp':250,'damage':30,'attack_type': 'claw',  'attack_sound':app_path('resources/audio/attack/claw.wav'),'speed': 2.5, 'resistance': 3, 'attack_radius': 69, 'notice_radius': 400, "update_radius":500},
    'spirit': {'health': 75,'exp':110,'damage':8,'attack_type': 'thunder', 'attack_sound':app_path('resources/audio/attack/fireball.wav'), 'speed': 3.5, 'resistance': 3, 'attack_radius': 69, 'notice_radius': 350, "update_radius":500},
    'bamboo': {'health': 100,'exp':120,'damage':6,'attack_type': 'leaf_attack', 'attack_sound':app_path('resources/audio/attack/slash.wav'), 'speed': 3, 'resistance': 3, 'attack_radius': 69, 'notice_radius': 300, "update_radius":500}}