from sprite_object import *

class ObjectHandler:
    def __init__(self, game):
        self.game = game
        self.sprite_list = []
        self.static_sprite_path = 'resources/sprites/static_sprites/'
        self.anim_sprite_path = 'resources/sprites/animated_sprites/'
        add_sprite = self.add_sprite

        add_sprite(SpriteObject(game))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'comum.png', pos=(1.5, 3), scale=1, shift=0))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'trash_can.png', pos=(3, 3), scale=.25, shift=0))
        add_sprite(AnimatedSprite(game))
        add_sprite(AnimatedSprite(game, pos=(1.5, 1.5)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(20, 14.5)))

    def update(self):
        [sprite.update() for sprite in self.sprite_list]

    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)