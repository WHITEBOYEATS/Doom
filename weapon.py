from sprite_object import *


class Weapon(AnimatedSprite):
    def __init__(self, game, path='resources/sprites/weapon/pistle/000.png', scale=0.4, animation_time=1, damage = 50):
        super().__init__(game=game, path=path, scale=scale, animation_time=animation_time)
        self.images = deque(
            [pygame.transform.smoothscale(img, (self.image.get_width() * scale, self.image.get_height()*scale))
             for img in self.images])
        self.weapon_pos = (HALF_WIDTH - self.images[0].get_width() // 2, HEIGHT - self.images[0].get_height())
        self.reloading = False
        self.scale= scale
        self.num_images = len(self.images)
        self.frame_counter = 0
        self.damage = damage

    # def change_gun(self):
    #     for event in pygame.event.get():
    #         if (event.type == pygame.KEYDOWN and event.key == pygame.K_1):
    #             self.path = 'resources/sprites/weapon/hand/00.png'
    #             # self.animation_time= 1
    #             # self.damage=100
    #             self.images = deque(
    #         [pygame.transform.smoothscale(img, (self.image.get_width() * self.scale, self.image.get_height()*self.scale))
    #          for img in self.images])
    #             self.num_images = len(self.images)

    def animate_shot(self):
        if self.reloading:
            self.game.player.shot = False
            if self.animation_trigger:
                self.images.rotate(-1)
                self.image = self.images[0]
                self.frame_counter += 1
                if self.frame_counter == self.num_images:
                    self.reloading = False
                    self.frame_counter = 0
    

    def draw(self):
        self.game.screen.blit(self.images[0], self.weapon_pos)

    def update(self):
        # self.change_gun()
        if not self.game.menu.button_clicked:
            self.check_animation_time()
            self.animate_shot()
        
