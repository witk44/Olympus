from cryptography.fernet import Fernet
import base64
import pygame,sys
from settings import *
from level import Level
code = b"""

import pygame,sys
from settings import *
from level import Level

class Game:
    def __init__(self) -> None:
        pygame.init()
        pygame.display.init()
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        pygame.display.set_caption("Olympus")
        self.clock = pygame.time.Clock()
        self.level = Level()
        main_sound = pygame.mixer.Sound('../audio/main.ogg')
        main_sound.set_volume(.5)
        main_sound.play(loops=-1)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or not self.level.player.alive:
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

if __name__ == "__main__":
    game = Game()
    game.run()

"""

key = Fernet.generate_key()
encryption_type = Fernet(key)
encrypted_message = encryption_type.encrypt(code)

decrypted_message = encryption_type.decrypt(encrypted_message)

exec(decrypted_message)