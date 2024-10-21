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
from pathfinding import *
from unique_sprite import *
from menu import *


class Game:
    def __init__(self):
        #initizes pygame and sets clock for frame rate and the screen size
        pygame.init()
        pygame.mouse.set_visible(False)
        self.screen = pygame.display.set_mode(RES)
        self.clock = pygame.time.Clock()
        self.delta_time = 1
        self.global_trigger = False
        self.global_event = pygame.USEREVENT + 0
        pygame.time.set_timer(self.global_event, 40)
        self.new_game()
        for i in range(1000):
            pygame.mixer.music.play()

    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.object_renderer = ObjectRendrer(self)
        self.raycasting = RayCasting(self)
        self.object_handler = ObjectHandler(self)
        keys = pygame.key.get_pressed()
        # self.weapon = Weapon(self)
        self.weapon = Weapon(self, path= 'resources/sprites/weapon/hand/00.png', animation_time= 1, damage=100)
        self.sound = Sound(self)
        self.pathfinding = PathFinding(self)
        self.menu = Menu(self)

    def update(self):
        
        self.player.update()
        self.raycasting.update()
        self.object_handler.update()
        self.weapon.update()
        pygame.display.flip()
        # sets the clock speed the the settings frame rate
        self.delta_time = self.clock.tick(FPS)
        pygame.display.set_caption(f'{self.clock.get_fps() :.1f}')
        
    def draw(self):
        # makes the screen black
        # self.screen.fill('black')
        self.object_renderer.draw()
        self.weapon.draw()
        # self.map.draw()
        # self.player.draw()
        # self.menu.draw()

    def check_events(self):
        self.global_trigger = False
        #this is the check to close them game which you can do by hitting the X in the corner or clicking the esc key
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == self.global_event:
                self.global_trigger = True
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_e): 
                if self.player.health < PLAYER_MAX_HEALTH:
                    self.player.health += 10
                    self.e_pressed = False
                    if self.player.health > PLAYER_MAX_HEALTH:
                        self.player.health = PLAYER_MAX_HEALTH
            
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_r):
                self.new_game()
            self.menu.check_opened(event)
            self.player.single_fire_event(event)


    def run(self):
        # functions it does while running
        while True:
            self.check_events()
            self.update()
            self.draw()



if __name__ == '__main__':
    game = Game()
    game.run()