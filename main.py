import pygame
import sys
from pygame.locals import *
from random import *
import traceback

import plane
import bullet
import enemy


def main():    
    pygame.init()
    pygame.mixer.init()
    
    life_image = 'image/life.png'
    bg_music = 'music/game_music.ogg'
    background = "image/background.png"
    bomb_music = 'music/use_bomb.wav'
    about_me = 'image/about_me.png'
    about_me_image = pygame.image.load(about_me)
    about_me_rect = about_me_image.get_rect()
    MyLife = pygame.image.load(life_image)
    Mybackground1 = pygame.image.load(background)
    life_rect = MyLife.get_rect()
    bg_size = 480, 700
    screen = pygame.display.set_mode(bg_size)
    pygame.display.set_caption("飞机大战")
    MyBullet = []
    Enemy = []
    kill = []
    score = 0
    score_font = pygame.font.Font("font/font.ttf", 36)
    num = 5
    num1 = 0
    num2 = 0
    num3 = 0
    harm = 1
    pygame.key.set_repeat(100, 100)
    clock = pygame.time.Clock()
    MyPlane = plane.Plane(bg_size)
    Enemy_group = pygame.sprite.Group()
    bg_music = pygame.mixer.Sound(bg_music)
    bomb_sound = pygame.mixer.Sound(bomb_music)
    bg_music.play(-1)
    super_Bullet = False
    running = True
    again = False
    My_Protection_cover = plane.Protection_cover(bg_size)
    paused = False
    pause_nor_image = pygame.image.load("image/pause_nor.png").convert_alpha()
    pause_pressed_image = pygame.image.load("image/pause_pressed.png").convert_alpha()
    resume_nor_image = pygame.image.load("image/resume_nor.png").convert_alpha()
    resume_pressed_image = pygame.image.load("image/resume_pressed.png").convert_alpha()
    again_image = pygame.image.load("image/again.png").convert_alpha()
    gameover_image = pygame.image.load("image/gameover.png").convert_alpha()
    me_image = pygame.image.load('image/me.png').convert_alpha()
    me_rect = me_image.get_rect()
    gameover_rect = gameover_image.get_rect()    
    again_rect = again_image.get_rect()    
    paused_rect = pause_nor_image.get_rect()
    paused_rect.left, paused_rect.top = bg_size[0] - paused_rect.width - 10, 10
    paused_image = pause_nor_image
    tnt_num = 10



    while running:
        if MyPlane.dead == True:
            MyPlane = plane.Plane(bg_size)
            MyPlane.not_dead = not MyPlane.not_dead
            MyPlane.life_num = oldLife
            again = True
            num4 = 0
            
            
        for event in pygame.event.get():
            if event.type == QUIT:
                bg_music.stop()
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and MyPlane.dead == False:
                if event.key == K_TAB:
                    MyPlane.not_dead = not MyPlane.not_dead
                if event.key == K_RETURN:
                    if harm < 11:
                        harm += 1
                    if harm >= 11 :
                        harm = 1 
                if event.key == K_SPACE:
                    if tnt_num > 0:
                        bomb_sound.play()
                        
                        for each in Enemy:
                            kill.append(each)
                            score += each.score
                        Enemy.clear()
                        Enemy_group = pygame.sprite.Group()
                        tnt_num -= 1
                        
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1 and paused_rect.collidepoint(event.pos):
                    paused = not paused
                    if paused:
                        bg_music.stop()
                    else:
                        bg_music.play(-1)
                        
            if event.type == MOUSEMOTION:
                if paused_rect.collidepoint(event.pos) == True:
                    if paused == True:
                        paused_image = resume_pressed_image
                    if paused == False:
                        paused_image = pause_pressed_image
                else:
                    if paused == True:
                        paused_image = resume_nor_image
                    if paused == True:
                        paused_image = pause_nor_image 
                        
                
                                        
        screen.blit(Mybackground1, (0, 0))
        key = pygame.key.get_pressed()
        if MyPlane.dead == False and paused == False:
            if key[K_w] or key[K_UP]:
                MyPlane.move([0, -1])
            if key[K_s] or key[K_DOWN]:
                MyPlane.move([0, 1])
            if key[K_a] or key[K_LEFT]:
                MyPlane.move([-1, 0])
            if key[K_d] or key[K_RIGHT]:
                MyPlane.move([1, 0])
            if key[K_j] or key[K_1]:
                if num1 == num:
                    temp = bullet.Bullet(MyPlane.rect.centerx, MyPlane.rect.top, harm)
                    music = pygame.mixer.Sound(temp.music)
                    music.play()
                    MyBullet.insert(0, temp)
                    num1 = 0
                num1 += 1
                    
            
        
        for each in Enemy:
            if each.disappear == True:
                Enemy.remove(each)
            elif paused == False:
                each.move()                
                if each.Enemytype == 'BigEnemy' and each.hit == False:
                    if num3 >= 5:
                        screen.blit(each.default_image[0], each.rect)
                    elif num3 <= 5:
                        screen.blit(each.default_image[1], each.rect)
                elif each.hit == False:
                    screen.blit(each.default_image[0], each.rect)
                else:
                    screen.blit(each.hit_image[0], each.rect)                
                    
        for each in MyBullet:
            if each.disappear == True:
                MyBullet.remove(each)    
            elif paused == False:
                each.move()
                screen.blit(each.image, each.rect)
        
        for x in MyBullet:
            for y in Enemy:
                if pygame.sprite.collide_rect(x, y):
                    MyBullet.remove(x)
                    y.life -= harm
                    break
                
        if MyPlane.not_dead == False:
            enemies_down = pygame.sprite.spritecollide\
            (MyPlane, Enemy_group, False, pygame.sprite.collide_mask)
        else:
            enemies_down = pygame.sprite.spritecollide\
            (My_Protection_cover, Enemy_group, False, pygame.sprite.collide_mask)
            
        if enemies_down:
            if MyPlane.not_dead == False and MyPlane.dead == False:
                MyPlane.life_num -= 1
                oldLife = MyPlane.life_num
                kill.append(MyPlane)
                MyPlane.dead = True
                tnt_num = 10
            for each in enemies_down:
                Enemy_group.remove(each)
                score += each.score
                try:
                    Enemy.remove(each)
                except:
                    pass
                each.dead()
                kill.append(each)        
        
    
        if (num2 % 30) == 0 and num2 != 0:
            x = randint(0, bg_size[0])            
            temp = enemy.SmallEnemy(bg_size)
            temp.init_image()
            temp.init_pos(randint(0, bg_size[0]), 0)
            Enemy.append(temp)
            Enemy_group.add(temp)
        if (num2 % 90) == 0 and num2 != 0:
            x = randint(0, bg_size[0])            
            temp = enemy.MidEnemy(bg_size)
            temp.init_image()
            temp.init_pos(randint(0, bg_size[0]), 0)
            Enemy.insert(0, temp)
            Enemy_group.add(temp)
        if (num2 % 250) == 0 and num2 != 0:
            x = randint(0, bg_size[0])            
            temp = enemy.BigEnemy(bg_size)
            temp.init_image()
            temp.init_pos(randint(0, bg_size[0]), 0)
            Enemy.append(temp)
            Enemy_group.add(temp)
            num2 = 0

        for k in kill:
            if len(k.dead_image) <= 0:
                kill.remove(k)
                continue
            else:
                screen.blit(k.dead_image[0], k.rect)
                del k.dead_image[0]
                       
        
        for each in Enemy:
            if each.life <= 0:
                each.dead()
                Enemy.remove(each)
                Enemy_group.remove(each)
                kill.append(each)
                score += each.score
                continue
            
            if each.life <= each.hitLife / 2 and each.hit == False:
                each.hit = True
        
        if num3 >= 10:
            num3 = 0 
        
        num2 += 1
        num3 += 1
        
        if MyPlane.not_dead == True and paused == False:
            My_Protection_cover.move\
            (MyPlane.rect.centerx,MyPlane.rect.centery)
            screen.blit(\
            My_Protection_cover.image,\
            My_Protection_cover.rect)
            
        if MyPlane.dead == False:
            if num3 <= 5:
                screen.blit(MyPlane.default_image[0], MyPlane.rect)
        
            elif num3 > 5:
                screen.blit(MyPlane.default_image[1], MyPlane.rect)        
            
        score_text = score_font.render("Score : %s" % str(score), True, (255, 0, 0))
        screen.blit(score_text, (10, 5))
        
    
        for i in range(0, MyPlane.life_num):
            screen.blit(MyLife, (0+(life_rect.w * i),bg_size[1]-life_rect.h))
            
        if MyPlane.life_num <= 0:
            game_over_text = score_font.render\
            ("Game Over" , True, (0, 0, 0))
            game_over_rect = game_over_text.get_rect()
            screen.blit(Mybackground1, (0, 0))            
            
            Enemy.clear()
            running = False
            bg_music.stop()
            is_about_me = False
            again_rect.left, again_rect.top =\
                ((bg_size[0]- again_rect.width) // 2, bg_size[1]//2-gameover_rect.height)
            gameover_rect.left , gameover_rect.top =\
                ((bg_size[0] - gameover_rect.width) // 2, bg_size[1]//2)
            about_me_rect.left, about_me_rect.top = \
                ((bg_size[0] - about_me_rect.width) // 2, bg_size[1]//2+about_me_rect.height)
            me_rect.left ,me_rect.top = (bg_size[0] - me_rect.width)//2, (bg_size[1]//2-me_rect.height-about_me_rect.height)
            
            
            while True:
                
                
                for event in pygame.event.get():
                    if event.type == QUIT:
                        bg_music.stop()
                        pygame.quit()
                        sys.exit()
                    if event.type == MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()
                        if again_rect.left < pos[0] < again_rect.right and \
                           again_rect.top < pos[1] < again_rect.bottom:
                            
                            main()
                        elif gameover_rect.left < pos[0] < gameover_rect.right and \
                             gameover_rect.top < pos[1] < gameover_rect.bottom:
                            pygame.quit()
                            sys.exit()
                        elif about_me_rect.left < pos[0] < about_me_rect.right and \
                            about_me_rect.top < pos[1] < about_me_rect.bottom:
                            is_about_me = not is_about_me

                
                
                game_over_rect = game_over_text.get_rect()
                screen.blit(Mybackground1, (0, 0))
                screen.blit\
                (game_over_text,((bg_size[0] - game_over_rect.width) // 2, bg_size[1]//2-100))                
                if is_about_me  == True:
                    screen.blit(me_image, me_rect)
                screen.blit(score_text,(0, 10))
                
                screen.blit(again_image, again_rect)
                screen.blit(gameover_image, gameover_rect)
                screen.blit(about_me_image, about_me_rect)
                pygame.display.flip()
                clock.tick(60) 
                    
        if again == True:
            num4 += 1
            if num4 == 600:
                del num4
                again = False
                MyPlane.not_dead = False
        
        pos = pygame.mouse.get_pos()
        if paused_rect.left < pos[0] < paused_rect.right and \
            paused_rect.top < pos[1] < paused_rect.bottom:        
            if paused == True:
                paused_image = resume_pressed_image
            if paused == False:
                paused_image = pause_pressed_image
        else:
            if paused == True:
                paused_image = resume_nor_image
            if paused == False:
                paused_image = pause_nor_image             
            
        
        screen.blit(paused_image, paused_rect)
        pygame.display.flip()
        clock.tick(60)
        
        
        


if __name__ == '__main__':
    try:
        main()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        pygame.quit()
        input()
