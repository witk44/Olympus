import pygame,sys
import level

from settings import *

class DeathScreen():
    def __init__(self):

        self.display_surface = pygame.display.get_surface()
        self.attribute_nr = 0
        self.font = pygame.font.Font(UI_FONT, 22)

        #dimensions
        self.height = self.display_surface.get_size()[1]*0.1
        self.width = self.display_surface.get_size()[0]//4
        self.item_list = []

        
    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            pygame.mixer.pause()
            new_game = NewGame()
            new_game.run()
    def display(self):
        
        self.input()
        full_width = self.display_surface.get_size()[0]
        l = (full_width // 2)-(self.width//2)

        t = self.display_surface.get_size()[1]*.5 - (self.width//5)
        self.rect = pygame.rect.Rect(l,t,self.width,self.height)
        pygame.draw.rect(self.display_surface,UI_BG_COLOR,self.rect)
        #attributes
        name = "You Died, LMAO"
        self.rect = pygame.rect.Rect(l,t,self.width,self.height)
        pygame.draw.rect(self.display_surface,UI_BG_COLOR,self.rect)
        self.display_names(self.display_surface,name,5)
        name = "Trashbag, Dogwater Player"
        self.display_names(self.display_surface,name,25)
        name = "Press Spacebar to restart"
        self.display_names(self.display_surface,name,45)
    
    def display_names(self,surface,name,height):
        color =  TEXT_COLOR
        name = name.capitalize()
        title_surf = self.font.render(name,False,color)
        title_rect = title_surf.get_rect(midtop = self.rect.midtop + pygame.math.Vector2(0,height))


        surface.blit(title_surf,title_rect)

class NewGame:
    def __init__(self) -> None:
        pygame.init()
        pygame.display.init()
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        pygame.display.set_caption("Olympus")
        self.clock = pygame.time.Clock()
        self.level = level.Level()
        main_sound = pygame.mixer.Sound('../audio/main.ogg')
        main_sound.set_volume(.5)
        main_sound.play(loops=-1)

    def run(self):
        while True:
            for event in pygame.event.get():
                if self.level.player.escape_key:
                    pygame.display.quit()
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        self.level.toggle_menu()
            self.screen.fill(WATER_COLOR)
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)