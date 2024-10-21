from sprite_object import *
from npc import *
from unique_sprite import *

class ObjectHandler:
    def __init__(self, game):
        self.game = game
        self.sprite_list = []
        self.npc_list = []
        self.unique_sprite_list = []
        self.npc_sprite_path = 'resources/sprites/npc/'
        self.static_sprite_path = 'resources/sprites/static_sprites/'
        self.anim_sprite_path = 'resources/sprites/animated_sprites/'
        self.static_unique_sprite_path = 'resources/sprites/unique_sprites'
        add_sprite = self.add_sprite
        add_npc = self.add_npc
        add_unique_sprite = self.add_unique_sprite
        self.npc_positions = {}
        self.unique_sprite_positions = {}

        add_sprite(SpriteObject(game))
        add_sprite(SpriteObject(game, path=self.static_sprite_path + 'comum.png', pos=(1.5, 3), scale=1, shift=0))
        # add_sprite(SpriteObject(game, path=self.static_sprite_path + 'trash_can.png', pos=(3, 3), scale=.5, shift=.5))
        add_sprite(AnimatedSprite(game))
        # add_sprite(AnimatedSprite(game, pos=(1.5, 1.5)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(20, 14.5)))
        add_unique_sprite(UniqueSprite(game))
        add_unique_sprite(UniqueSprite(game, pos=(1.5, 1.5)))



        #npc
        add_npc(NPC(game))
        add_npc(NPC(game, pos=(11.4, 4.5)))

    def update(self):
        self.npc_positions = {npc.map_pos for npc in self.npc_list if npc.alive}
        self.unique_sprite_positions = {unique_sprite.map_pos for unique_sprite in self.unique_sprite_list if unique_sprite.alive}

        [sprite.update() for sprite in self.sprite_list]
        [npc.update() for npc in self.npc_list]
        [unique_sprite.update() for unique_sprite in self.unique_sprite_list]

    def add_npc(self, npc):
        self.npc_list.append(npc)

    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)

    def add_unique_sprite(self, unique_sprite):
        self.unique_sprite_list.append(unique_sprite)