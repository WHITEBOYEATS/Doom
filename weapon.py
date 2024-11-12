import pygame
from settings import *
import os
from collections import deque
from projectile import *

class Weapon:
    def __init__(self, game, pathOne='resources/sprites/weapon/hand/00.png', pathTwo='resources/sprites/weapon/pistle/000.png', scale=0.4, animation_time=1, damage=50, weapon_number=1):
        self.game = game
        self.player = game.player
        self.scale = scale
        self.animation_time = animation_time
        self.damage = damage
        self.animation_time_prev = pygame.time.get_ticks()
        
        self.weapons = {
            1: {
                'path': pathOne,
                'damage': 100,
                'scale' : .4
            },
            2: {
                'path': pathTwo,
                'damage': 50,
                'scale' : .4
            }
        }
        
        self.images = {}
        for key, weapon in self.weapons.items():
            path = weapon['path']
            images = self.get_images(path)
            scaled_images = deque([pygame.transform.smoothscale(img, (img.get_width() * self.scale, img.get_height() * self.scale)) for img in images])
            self.images[key] = scaled_images
        
        self.current_weapon = 1
        self.image_queue = self.images[self.current_weapon]
        self.image = self.image_queue[0]
        self.weapon_pos = (HALF_WIDTH - self.image.get_width() // 2, HEIGHT - self.image.get_height())
        self.frame_counter = 0
        self.reloading = False

    def imput(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                self.change_weapon(1)
            elif event.key == pygame.K_2:
                self.change_weapon(2)

    def change_weapon(self, weapon_number):
        if self.current_weapon != weapon_number:
            self.current_weapon = weapon_number
            self.image_queue = self.images[self.current_weapon]
            self.image = self.image_queue[0]
            self.weapon_pos = (HALF_WIDTH - self.image.get_width() // 2, HEIGHT - self.image.get_height())
            self.frame_counter = 0
            self.damage = self.weapons[self.current_weapon]['damage']
            self.scale = self.weapons[self.current_weapon]['scale']

    def get_sprite_projection(self):
        proj = SCREEN_DIST / self.norm_dist * self.SPRITE_SCALE
        proj_width, proj_height = proj * self.IMAGE_RATIO, proj
        image = pygame.transform.scale(self.image, (proj_width, proj_height))
        self.sprite_half_width = proj_width // 2
        height_shift = proj_height
        pos = self.screen_x - self.sprite_half_width, HALF_HEIGHT - proj_height // 2 + height_shift
        self.game.raycasting.objects_to_render.append((self.norm_dist, image, pos))
    
    def shoot(self):
        angle = self.player.angle
        x = HALF_WIDTH
        y = HALF_HEIGHT
        Projectile(self.game, x, y)
        
    def get_sprite(self):
        dx = self.x - self.player.x
        dy = self.y - self.player.y
        self.dx, self.dy = dx, dy
        self.theta = math.atan2(dy, dx)
        delta = self.theta - self.player.angle
        if (dx > 0 and self.player.angle > math.pi) or (dx < 0 and dy < 0):
            delta += math.tau
        delta_ray = delta / DELTA_ANGLE
        self.screen_x = (HALF_NUM_RAYS + delta_ray) * SCALE
        self.dist = math.hypot(dx, dy)
        self.norm_dist = self.dist * math.cos(delta)
        if -self.IMAGE_HALF_WIDTH < self.screen_x < (WIDTH + self.IMAGE_HALF_WIDTH) and self.norm_dist > 0.5:
            self.get_sprite_projection()

    def animate_shot(self):
        if self.reloading:
            self.game.player.shot = False
            if self.animation_trigger:
                self.image_queue.rotate(-1)
                self.image = self.image_queue[0]
                self.frame_counter += 1
                if self.frame_counter == len(self.image_queue):
                    self.reloading = False
                    self.frame_counter = 0

    def draw(self):
        self.game.screen.blit(self.image_queue[0], self.weapon_pos)

    def update(self):
        self.check_animation_time()
        self.animate_shot()
        if self.reloading and not self.game.projectile.alreadyProjectile == True:
            self.game.projectile.projectile()

    def check_animation_time(self):
        self.animation_trigger = False
        time_now = pygame.time.get_ticks()
        if time_now - self.animation_time_prev > self.animation_time:
            self.animation_time_prev = time_now
            self.animation_trigger = True

    def get_images(self, path):
        images = deque()
        try:
            for file_name in os.listdir(path.rsplit('/', 1)[0]):
                if os.path.isfile(os.path.join(path.rsplit('/', 1)[0], file_name)):
                    img = pygame.image.load(os.path.join(path.rsplit('/', 1)[0], file_name)).convert_alpha()
                    images.append(img)
        except FileNotFoundError:
            for file_name in os.listdir('_internal/' + path.rsplit('/', 1)[0]):
                if os.path.isfile(os.path.join('_internal/' + path.rsplit('/', 1)[0], file_name)):
                    img = pygame.image.load('_internal/' + os.path.join(path.rsplit('/', 1)[0], file_name)).convert_alpha()
                    images.append(img)
        return images
