import pygame
from settings import *

class ObjectRendrer:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.wall_textures = self.load_wall_textures()
        try:
            self.sky_image = self.get_texture('_internal/resources/textures/new piskel-1.png.png', (WIDTH, HALF_HEIGHT))
        except:
            self.sky_image = self.get_texture('resources/textures/new piskel-1.png.png', (WIDTH, HALF_HEIGHT))
        self.sky_offset = 0
        try:
            self.blood_screen = self.get_texture('_internal/resources/textures/blood_screen.png', (RES))
        except:
            self.blood_screen = self.get_texture('resources/textures/blood_screen.png', (RES))
        try:
            self.border = self.get_texture('_internal/resources/textures/border.png', (RES))
        except:
            self.border = self.get_texture('resources/textures/border.png', (RES))
        self.digit_size = 90
        try:
            self.digit_images = [self.get_texture(f'resources/textures/digits/{i}.png', [self.digit_size] * 2)
                                 for i in range(11)]
        except:
            self.digit_images = [self.get_texture(f'_internal/resources/textures/digits/{i}.png', [self.digit_size] * 2)
                                 for i in range(11)]
        try:
            self.health = self.get_texture('resources/textures/health.png', (238, 59))
        except:
            self.health = self.get_texture('_internal/resources/textures/health.png', (238, 59))
        try:
            self.health_front = self.get_texture('resources/textures/health_front.png', (238, 59))
        except:
            self.health_front = self.get_texture('_internal/resources/textures/health_front.png', (238, 59))
        self.digits = dict(zip(map(str, range(11)), self.digit_images))
        try:
            self.game_over_image = self.get_texture('resources/textures/game_over.png', RES)
        except:
            self.game_over_image = self.get_texture('_internal/resources/textures/game_over.png', RES)


    def draw(self):
        self.draw_background()
        self.render_game_objects()
        self.draw_menu()
        self.screen.blit(self.border, (0, 0))
        self.draw_player_health()
        

    def draw_menu(self):
        self.game.menu.draw()

    def game_over(self):
        self.screen.blit(self.game_over_image, (0, 0))

    def draw_player_health(self):
        health = str(self.game.player.health)
        for i, char in enumerate(health):
            if self.game.player.health == 100:
                self.screen.blit(self.digits[char], (i * self.digit_size, 15))
            elif self.game.player.health < 10:
                 self.screen.blit(self.digits[char], (i * self.digit_size + self.digit_size + self.digit_size , 15))
            else:
                self.screen.blit(self.digits[char], (i * self.digit_size + self.digit_size, 15))
        self.screen.blit(self.health, (50, 140))
        pygame.draw.rect(self.screen, (100, 0, 0), (50, 141, 238, self.game.player.health//1.76))
        self.screen.blit(self.health_front, (50, 140))
        self.screen.blit(self.digits['10'], (3 * self.digit_size, 15))

    def player_damage(self):
        self.screen.blit(self.blood_screen, (0, 0))

    def draw_background(self):
        if not self.game.menu.button_clicked:
            self.sky_offset = (self.sky_offset + 4.5 * self.game.player.rel) % WIDTH
        if self.game.menu.button_clicked:
            self.sky_offset = (self.sky_offset + 4.5 * 10) % WIDTH
        self.screen.blit(self.sky_image, (-self.sky_offset, 0))
        self.screen.blit(self.sky_image, (-self.sky_offset + WIDTH, 0))

        pygame.draw.rect(self.screen, FLOOR_COLOR, (0, HALF_HEIGHT, WIDTH, HEIGHT))

    def render_game_objects(self):
        list_objects = sorted(self.game.raycasting.objects_to_render, key=lambda t: t[0], reverse=True)
        for depth, image, pos in list_objects:
            self.screen.blit(image, pos)

    @staticmethod
    def get_texture(path, res=(TEXTURE_SIZE, TEXTURE_SIZE)):
        try:
            texture = pygame.image.load(path).convert_alpha()
        except:
            texture = pygame.image.load('_internal' + path).convert_alpha()
        return pygame.transform.scale(texture, res)
      
    
    def load_wall_textures(self):
        try:
            return{
                1: self.get_texture('_internal/resources/textures/1.png'),
                2: self.get_texture('_internal/resources/textures/2.png'),
                3: self.get_texture('_internal/resources/textures/3.png'),
                4: self.get_texture('_internal/resources/textures/4.png'),
                5: self.get_texture('_internal/resources/textures/5.png'),
                6: self.get_texture('_internal/resources/textures/6.png'),
                7: self.get_texture('_internal/resources/textures/7.png'),
                8: self.get_texture('_internal/resources/textures/8.png'),
                9: self.get_texture('_internal/resources/textures/9.png'),
                10: self.get_texture('_internal/resources/textures/10.png'),
                11: self.get_texture('_internal/resources/textures/11.png'),
                12: self.get_texture('_internal/resources/textures/12.png'),
                13: self.get_texture('_internal/resources/textures/13.png'),
            }
        except:
            return{
                1: self.get_texture('resources/textures/1.png'),
                2: self.get_texture('resources/textures/2.png'),
                3: self.get_texture('resources/textures/3.png'),
                4: self.get_texture('resources/textures/4.png'),
                5: self.get_texture('resources/textures/5.png'),
                6: self.get_texture('resources/textures/6.png'),
                7: self.get_texture('resources/textures/7.png'),
                8: self.get_texture('resources/textures/8.png'),
                9: self.get_texture('resources/textures/9.png'),
                10: self.get_texture('resources/textures/10.png'),
                11: self.get_texture('resources/textures/11.png'),
                12: self.get_texture('resources/textures/12.png'),
                13: self.get_texture('resources/textures/13.png'),
            }
