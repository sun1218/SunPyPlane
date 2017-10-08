import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, num):
        pygame.sprite.Sprite.__init__(self)
        self.music = 'music/bullet.wav'
        self.image_str = 'image/bullet%s.png'%(num)
        self.image = pygame.image.load(self.image_str).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = ((x*2)-self.rect.w)//2, y
        self.speed = 12
        self.disappear = False
        self.mask = pygame.mask.from_surface(self.image)
        

    def move(self):
        self.rect.top -= self.speed
        if self.rect.top < 0:
            self.disappear = True