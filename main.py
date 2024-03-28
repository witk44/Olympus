from cryptography.fernet import Fernet
import base64
import pygame,sys
from resources.code.settings import *
from resources.code.level import Level
from resources.code.main_menu import MainMenu
# code = b"""

import pygame,sys
from resources.code.settings import *
from resources.code.level import Level
from resources.code.main_menu import MainMenu
class Game:
    def __init__(self) -> None:
        pygame.init()
        pygame.display.init()
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        pygame.display.set_caption("Olympus")
        self.display_loading_screens()
        self.main_menu = MainMenu()
        self.level = Level()
        self.start_game = False
        main_sound = pygame.mixer.Sound(app_path('resources/audio/main.ogg'))
        main_sound.set_volume(.5)
        main_sound.play(loops=-1)

    def run(self):
        while True:
            if self.start_game:
                self.main_menu.display()
                self.start_game != self.start_game
            else:
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

    def display_loading_screens(self):
        imp = pygame.image.load(app_path("resources/graphics/PyrateGames.jpg")).convert_alpha()
        imp = pygame.transform.scale(imp, (int(pygame.display.get_surface().get_size()[0]//2), int(pygame.display.get_surface().get_size()[1])//1))
        rect = imp.get_rect()
        rect.center = (pygame.display.get_surface().get_size()[0]//2, pygame.display.get_surface().get_size()[1]//2)
        self.screen.blit(imp,rect)
        pygame.display.flip()
        self.clock = pygame.time.Clock()
        self.clock.tick(.5)
        self.screen.fill((0,0,0))
        imp = pygame.image.load(app_path("resources/graphics/Olympus_loading_screen.jpg")).convert_alpha()
        imp = pygame.transform.scale(imp, (int(pygame.display.get_surface().get_size()[0]//2), int(pygame.display.get_surface().get_size()[1])//1.5))
        rect = imp.get_rect()
        rect.center = (pygame.display.get_surface().get_size()[0]//2, pygame.display.get_surface().get_size()[1]//2)
        self.screen.blit(imp,rect)
        pygame.display.flip()
        self.clock.tick(.5)
if __name__ == "__main__":
    game = Game()
    game.run()

# """

# key = Fernet.generate_key()
# encryption_type = Fernet(key)
# encrypted_message = encryption_type.encrypt(code)

# decrypted_message = encryption_type.decrypt(encrypted_message)

# exec(decrypted_message)