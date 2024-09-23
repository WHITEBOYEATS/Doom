import pygame, sys
from setting import *
from map import *
from player import *
from raycasting import *
from object_renderer import *
from sprite_object import *
from object_handler import *
from weapon import *
from sound import *


class Game:
    def __init__(self):
        #initizes pygame and sets clock for frame rate and the screen size
        pygame.init()
        pygame.mouse.set_visible(False)
        self.screen = pygame.display.set_mode(RES)
        self.clock = pygame.time.Clock()
        self.delta_time = 1
        self.new_game()

    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.object_renderer = ObjectRendrer(self)
        self.raycasting = RayCasting(self)
        self.object_handler = ObjectHandler(self)
        self.weapon = Weapon(self)
        self.sound = Sound(self)

    def update(self):
        self.player.update()
        self.raycasting.update()
        self.object_handler.update()
        self.weapon.update()
        pygame.display.flip()
        # sets the clock speed the the settings frame rate
        if self.clock.get_fps() > 60:
            self.delta_time = self.clock.tick(FPS)
        elif self.clock.get_fps() < 60:
            self.delta_time = self.clock.tick(30)
        else:
            self.delta_time = self.clock.tick(FPS)
        pygame.display.set_caption(f'{self.clock.get_fps() :.1f}')
        

    def check_events(self):
        #this is the check to close them game which you can do by hitting the X in the corner or clicking the esc key
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
            self.player.single_fire_event(event)

    def draw(self):
        # makes the screen black
        # self.screen.fill('black')
        self.object_renderer.draw()
        self.weapon.draw()
        # self.map.draw()
        # self.player.draw()

    def run(self):
        # functions it does while running
        while True:
            self.check_events()
            self.update()
            self.draw()

if __name__ == '__main__':
    game = Game()
    game.run()