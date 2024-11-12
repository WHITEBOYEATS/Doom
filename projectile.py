import pygame
import math
from settings import *

class Projectile:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.x, self.y = self.xy = 600, HALF_HEIGHT+100
        self.width, self.height = self.size = 0, 0
        self.image = self.game.object_renderer.get_texture('resources/textures/1.png', (100, 100))
        self.rect = pygame.rect.Rect(self.xy, self.size)
        # self.image = pygame.transform.scale(self.screen, self.xy)
        self.originalImage = self.image
        self.projectileAlive = False

    def projectile(self):
        self.image = self.originalImage
        self.angle = self.game.player.angle
        print(self.game.player.angle)
        self.width, self.height = self.size = 100, 100
        self.x, self.y = self.xy = 600, HALF_HEIGHT+100
        self.xy = self.x - (self.width/2), self.y
        self.rect.update(self.xy, self.size)
        self.projectileAlive = True
        self.alreadyProjectile = True
        
        print(self.alreadyProjectile, self.size, self.xy)
        


    def update(self):
        if self.width >= 1 or self.height >= 1:
            self.x += math.cos(self.game.player.angle)
            print(self.game.player.angle)
            self.width -= 5
            self.height -= 5
            self.size = self.width, self.height
            self.xy = self.x, self.y - (self.height/2)
            self.rect.update(self.xy, self.size)
            # self.image.transfrom()
            # self.x = self.originalX-(self.width*.5)
            # self.y = self.originalY-(self.height*.5)
            self.image = pygame.transform.scale(self.image, self.size)
            self.screen.blit(self.image, self.rect)
            pygame.draw.line(self.screen, "red", (HALF_WIDTH, HALF_HEIGHT), (HALF_WIDTH, HALF_HEIGHT + 100))
            self.screen.blit(self.image, (-100, 0))
            
        else:
            self.alreadyProjectile = False
            
            
        # if self.width <= 0 and self.height <= 0 and self.projectileAlive:
        #     self.projectileAlive = False
            

    def draw(self):
        self.screen.blit(self.image, self.rect)
            