WIDTH    = 1240
HEIGHT   =  600  #800
FPS      = 90
TILESIZE = 64

BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 200
ENERGY_BAR_WIDTH = 140
ITEM_BOX_SIZE = 100
UI_FONT = '../graphics/font/neon.ttf'
UI_FONT_SIZE = 16

# general colors
WATER_COLOR = '#71ddee'
UI_BG_COLOR = '#222222'
UI_BORDER_COLOR = 'gray'
TEXT_COLOR = '#EEEEEE'
 
# ui colors
HEALTH_COLOR = 'red'
ENERGY_COLOR = 'green'
UI_BORDER_COLOR_ACTIVE = 'gold'

weapon_data = {
    'sword': {'cooldown': 100, 'damage': 15,'graphic':'../graphics/weapons/sword/full.png'},
    'bigsword': {'cooldown': 400, 'damage': 30,'graphic':'../graphics/weapons/bigsword/full.png'},
    'axe': {'cooldown': 300, 'damage': 20, 'graphic':'../graphics/weapons/axe/full.png'},
    'katana':{'cooldown': 50, 'damage': 8, 'graphic':'../graphics/weapons/katana/full.png'},
    'lance':{'cooldown': 150, 'damage': 10, 'graphic':'../graphics/weapons/lance/full.png'}}

magic_data = {
    'lightning': {'strength': 20,'cost': 20,'graphic':'../graphics/particles/lightning_ball/tile000.png'},
    'heal' : {'strength': 10,'cost': 20,'graphic':'../graphics/particles/heal/tile000.png'}}

monster_data = {
    'squid': {'health': 100,'exp':100,'damage':20,'attack_type': 'slash', 'attack_sound':'../audio/attack/slash.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 80, 'notice_radius': 360},
    'raccoon': {'health': 300,'exp':250,'damage':40,'attack_type': 'claw',  'attack_sound':'../audio/attack/claw.wav','speed': 1, 'resistance': 3, 'attack_radius': 120, 'notice_radius': 400},
    'spirit': {'health': 100,'exp':110,'damage':8,'attack_type': 'thunder', 'attack_sound':'../audio/attack/fireball.wav', 'speed': 4, 'resistance': 3, 'attack_radius': 60, 'notice_radius': 350},
    'bamboo': {'health': 70,'exp':120,'damage':6,'attack_type': 'leaf_attack', 'attack_sound':'../audio/attack/slash.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 50, 'notice_radius': 300}}