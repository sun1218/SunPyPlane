import pygame
from random import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.default_image = []
        self.hit_image = []
        self.dead_image = []
        self.disappear = False
        self.hit = False
        self.hitLife = self.life // 2
        self.isEnemy = True
        

    def init_image(self):
        for each in self.default_image_str:
            image = pygame.image.load(each).convert_alpha()            
            self.default_image.append(image)
        for each in self.hit_image_str:
            image = pygame.image.load(each).convert_alpha()            
            self.hit_image.append(image)
        for each in self.dead_image_str:
            image = pygame.image.load(each).convert_alpha()            
            self.dead_image.append(image)
        self.rect = self.default_image[0].get_rect()
        self.mask = pygame.mask.from_surface(self.default_image[0])
            
            

    def init_pos(self, x, y):
        if self.rect.w > x:
            self.rect.left, self.rect.top = self.rect.w, y - self.rect.height
        if x > self.bg_size[0] - self.rect.w:
            self.rect.left, self.rect.top = x - self.rect.w, y - self.rect.height
        else:
            self.rect.left, self.rect.top = x, y - self.rect.height
        
    def move(self):
        self.rect.top += self.speed
        if self.bg_size[1] + self.rect.height < self.rect.bottom:
            self.disappear = True

    def dead(self):
        self.dead_sound = pygame.mixer.Sound(self.dead_music_str)
        self.dead_sound.play()
    

class SmallEnemy(Enemy):
    def __init__(self, bg_size):
        self.bg_size = bg_size
        self.default_image_str = ['image/enemy1.png']
        self.hit_image_str = []
        self.dead_image_str = \
        ['image/enemy1_down1.png','image/enemy1_down2.png',\
         'image/enemy1_down3.png', 'image/enemy1_down4.png']
        self.dead_music_str = 'music/enemy1_down.wav'
        self.life = 1
        self.score = 1000
        x = randint(0, bg_size[0])
        self.Enemytype = 'SmallEnemy'
        self.speed = 3
        super().__init__()
        

class MidEnemy(Enemy):
    def __init__(self, bg_size):
        self.bg_size = bg_size
        self.default_image_str = ['image/enemy2.png']
        self.hit_image_str = ['image/enemy2_hit.png']
        self.dead_image_str = \
        ['image/enemy2_down1.png','image/enemy2_down2.png',\
         'image/enemy2_down3.png', 'image/enemy2_down4.png']
        self.dead_music_str = 'music/enemy2_down.wav'
        self.life = 10
        self.score = 3000
        self.Enemytype = 'MidEnemy'
        self.speed = 2
        super().__init__()


        
class BigEnemy(Enemy):
    def __init__(self, bg_size):
        self.bg_size = bg_size
        self.default_image_str = ['image/enemy3_n1.png','image/enemy3_n2.png']
        self.hit_image_str = ['image/enemy3_hit.png']
        self.dead_image_str = \
        ['image/enemy3_down1.png','image/enemy3_down2.png',\
         'image/enemy3_down3.png','image/enemy3_down4.png',\
         'image/enemy3_down5.png','image/enemy3_down6.png']        
        self.dead_music_str = 'music/enemy3_down.wav'
        self.life = 20
        self.score = 5000
        x = randint(0, bg_size[0])
        self.Enemytype = 'BigEnemy'
        self.speed = 1
        super().__init__()
        

        

    