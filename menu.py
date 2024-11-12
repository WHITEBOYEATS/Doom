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
        self.next_slider_clicked = False
        self.menu_screen = 1
        pygame.font.get_default_font()
        self.x, self.y = HALF_WIDTH-25, HALF_HEIGHT-100
        
        try:
            self.menu_background = self.game.object_renderer.get_texture('resources/textures/menu_background.png', (RES))
        except:
            self.menu_background = self.game.object_renderer.get_texture('_internal/resources/textures/menu_background.png', (RES))
        

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
            
        if (pygame.mouse.get_pressed(num_buttons=3)) == (True, False, False):
            self.next_slider_clicked = True
        else:
            self.next_slider_clicked = False
            
    
    def menu_buttons(self, varible, color, color_two, x, y, width, height):
        rect = pygame.rect.Rect(x, y, width , height)
        pygame.draw.rect(self.screen, color , rect)
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if mouse_x >= x and mouse_x <= (x+width) and mouse_y >= y and mouse_y <= (y+height) and self.next_button_clicked:
            if varible == 1:
                if self.menu_screen == 1:
                    self.menu_screen += 1
                else:
                    self.menu_screen -= 1
            if varible == 2:
                self.game.exit()
            pygame.draw.rect(self.screen, color_two , rect)
        elif mouse_x >= x and mouse_x <= (x+width) and mouse_y >= y and mouse_y <= (y+height) and varible == 2:
            pygame.draw.rect(self.screen, color_two, rect, 10)
            # if self.menu_screen == 1:
            # elif self.menu_screen == 2:
            #     self.menu_screen == 1
        
    def menu_slider(self, varible, color, x, y, min_x, min_y, max_x, max_y, width, height):
        rect_max_min = pygame.rect.Rect(min_x, min_y, 500, 60)
        rect = pygame.rect.Rect(self.x, self.y, width , height)
       
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if mouse_x >= (min_x) and mouse_x <= (max_x+width) and mouse_y >= (min_y) and mouse_y <= (min_y+height) and self.next_slider_clicked:
            self.x = mouse_x - 25
            self.game.volume = pygame.mixer.music.set_volume((((self.x- 400)//10)*2)/100)
            
            # this changes the bounds
            if self.x > max_x:
                self.x = max_x
            if self.x <  min_x:
                self.x = min_x
            if self.y > max_y:
                self.y = min_y + y
            if self.y < min_y:
                self.y = min_y
        pygame.draw.rect(self.screen, "red" , rect_max_min)
        pygame.draw.rect(self.screen, color , rect)
        
        

    def draw(self):
        
        if self.button_clicked:
            pygame.mouse.set_visible(True)
            self.screen.blit(self.menu_background, (0 ,0))
            self.menu_buttons(1, (200,200,200), (50,50,50), 1100, 20, 100, 50)
            if self.menu_screen == 2:
                self.screen.blit(self.menu_background, (0 ,0))   
                pygame.draw.rect(self.screen, "black",(HALF_WIDTH - (HALF_WIDTH*.5) ,0, self.menu_size_width, self.menu_size_height))
                self.menu_buttons(2, "green", "gray", HALF_WIDTH-75, HALF_HEIGHT-30, 150, 60)
                self.menu_slider(1, "gray", HALF_WIDTH-25, 250, 400, HALF_HEIGHT-100, 850, 250, 50, 60)
                # self.menu_buttons(self.menu_screen, (200,200,200), (50,50,50), 1100, 20, 100, 50)
            
        else:
            pygame.mouse.set_visible(False)