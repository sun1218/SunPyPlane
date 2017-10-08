import pygame


class Plane(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)
        self.default_image_str = ['image/me1.png','image/me2.png']
        self.dead_image_str =\
        ['image/me_destroy_1.png', 'image/me_destroy_2.png',\
         'image/me_destroy_3.png', 'image/me_destroy_4.png'] 
        self.default_image = []
        self.dead_image = []
        self.music = 'bullet.wav'
        self.speed = 5
        self.bg_size = bg_size
        self.life_num = 3
        for each in self.default_image_str:
            image = pygame.image.load(each).convert_alpha()            
            self.default_image.append(image)
    
        for each in self.dead_image_str:
            image = pygame.image.load(each).convert_alpha()            
            self.dead_image.append(image)        
        
        self.rect = self.default_image[0].get_rect()
        self.rect.left, self.rect.top = \
            (bg_size[0] - self.rect.width) // 2, bg_size[1] - self.rect.height - 60
        self.mask = pygame.mask.from_surface(self.default_image[0])
        
        self.dead_music_str = 'music/me_down.wav'
        self.not_dead = False
        self.dead = False
        self.isEnemy = False

    def move(self, side):
        self.rect = self.rect.move\
            ([side[0] * self.speed, side[1] * self.speed])
        if self.rect.right > self.bg_size[0]:
            self.rect.left = self.bg_size[0] - self.rect.width
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > self.bg_size[1] - 60:
            self.rect.top = self.bg_size[1] - self.rect.height - 60
        if self.rect.top < 0:
            self.rect.top = 0
            
    def dead(self):
        self.dead_sound = pygame.mixer.Sound(self.dead_music_str)
        self.dead_sound.play()
        
class Protection_cover(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)
        self.bg_size = bg_size
        self.image =  pygame.image.load('image/Protection_cover.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        
    def move(self,centerx,centery):
        self.rect.centerx,\
        self.rect.centery =\
        centerx, centery          
    