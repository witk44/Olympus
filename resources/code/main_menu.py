
import pygame,sys
import resources.code.level
from resources.code.settings import *

class MainMenu:
    def __init__(self):
        self.screen_width = pygame.display.get_window_size()[0]
        self.screen_height = pygame.display.get_window_size()[1]
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.font = pygame.font.Font(None, 36)
        self.menu_options = ["New Game", "Load Game", "Options", "Quit"]
        self.selected_option = 0
        self.is_displaying = True
    
    def display(self):
       while self.is_displaying:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        # Move selection left
                        self.selected_option = (self.selected_option - 1) % len(self.menu_options)
                    elif event.key == pygame.K_d:
                        # Move selection right
                        self.selected_option = (self.selected_option + 1) % len(self.menu_options)
                    elif event.key == pygame.K_SPACE:
                        # Submit selection
                        selected_text = self.menu_options[self.selected_option]
                        self.is_displaying = False
            imp = pygame.image.load(app_path("resources/graphics/Olympus_loading_screen.jpg")).convert_alpha()
            imp = pygame.transform.scale(imp, (int(pygame.display.get_surface().get_size()[0]//2), int(pygame.display.get_surface().get_size()[1])//1.5))
            rect = imp.get_rect()
            rect.center = (pygame.display.get_surface().get_size()[0]//2, pygame.display.get_surface().get_size()[1]//2)
            self.screen.blit(imp,rect)
     
            # Draw the menu options
            for i, option_text in enumerate(self.menu_options):
                x = self.screen_width // 3.5
                y = self.screen_height // 2.2
                text = self.font.render(option_text, True, (0, 0, 0))
                if i == self.selected_option:
                    # Draw a highlight box around the selected option
                    pygame.draw.rect(screen, (255, 0, 0), text.get_rect(x=x, y=y, width=text.get_width(), height=text.get_height()), 2)
            
            
            # Update the display
            pygame.display.flip() 