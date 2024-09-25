import pygame

class Sound:
    def __init__(self, game):
        self.game = game
        pygame.mixer.init()
        self.path = 'resources/sound/'
        try:
            self.shotgun = pygame.mixer.Sound(self.path + 'shotgun.wav')
            self.npc_pain = pygame.mixer.Sound(self.path + 'shotgun.wav')
            self.npc_death = pygame.mixer.Sound(self.path + 'shotgun.wav')
            self.npc_shot = pygame.mixer.Sound(self.path + 'shotgun.wav')
            self.play_pain = pygame.mixer.Sound(self.path + 'shotgun.wav')
            self.theme = pygame.mixer.music.load(self.path + 'shotgun.wav')
        except:
            self.shotgun = pygame.mixer.Sound('_internal/'+ self.path + 'shotgun.wav')