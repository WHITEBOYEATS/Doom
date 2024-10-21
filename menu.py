import pygame
from settings import *

class Menu:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.menu_size_height = HEIGHT
        self.menu_size_width = HALF_WIDTH
        self.button_clicked = False
        self.next_button_clicked = False
        self.menu_screen = 1
        
        try:
            self.menu_screen = self.game.object_renderer.get_texture('resources/textures/menu_background.png', (RES))
        except:
            self.menu_screen = self.game.object_renderer.get_texture('_internal/resources/textures/menu_background.png', (RES))
        

    def check_opened(self, event):
        if not self.button_clicked and (event.type == pygame.KEYDOWN and event.key == pygame.K_TAB):
                self.button_clicked = True
                self.menu_screen = 1
        elif self.button_clicked and (event.type == pygame.KEYDOWN and event.key == pygame.K_TAB):
                self.button_clicked = False

        if self.button_clicked and (event.type == pygame.KEYDOWN and event.key == pygame.K_1):
            self.menu_screen = 1
        if self.button_clicked and (event.type == pygame.KEYDOWN and event.key == pygame.K_2):
            self.menu_screen = 2

        if not self.next_button_clicked and (event.type == pygame.MOUSEBUTTONDOWN):
            self.next_button_clicked = True
        else:
            self.next_button_clicked = False
            
    
    def menu_buttons(self, varible, color, color_two, x, y, width, height):
        rect = pygame.rect.Rect(x, y, width , height)
        self.varible = varible
        pygame.draw.rect(self.screen, color , rect)
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if mouse_x >= x and mouse_x <= (x+width) and mouse_y >= y and mouse_y <= (y+height) and self.next_button_clicked:
            if self.menu_screen == 1:
                self.menu_screen += 1
            else:
                self.menu_screen -= 1
            pygame.draw.rect(self.screen, color_two , rect)
            # if self.menu_screen == 1:
            # elif self.menu_screen == 2:
            #     self.menu_screen == 1
        

    def draw(self):
        menu_screen = self.game.object_renderer.get_texture('resources/textures/menu_background.png', (RES))
        if self.button_clicked:
            pygame.mouse.set_visible(True)
            self.screen.blit(menu_screen, (0 ,0))
            self.menu_buttons(self.menu_screen, (200,200,200), (50,50,50), 1100, 20, 100, 50)
            if self.menu_screen == 2:
                self.screen.blit(menu_screen, (0 ,0))   
                pygame.draw.rect(self.screen, "black",(HALF_WIDTH - (HALF_WIDTH*.5) ,0, self.menu_size_width, self.menu_size_height))
                
                # self.menu_buttons(self.menu_screen, (200,200,200), (50,50,50), 1100, 20, 100, 50)
            
        else:
            pygame.mouse.set_visible(False)