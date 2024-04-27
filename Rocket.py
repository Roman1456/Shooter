import pygame
from Bullet import Bullet



class Rocket:
    def __init__(self,x,y,w,h,img,speed):
        self.photo = pygame.transform.scale(pygame.image.load(img), (w, h))
        self.hitbox = self.photo.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y
        self.speed = speed
        self.patronu=[]

    def draw(self, window):
        window.blit(self.photo, (self.hitbox.x, self.hitbox.y))
        for bullet in self.patronu:
            bullet.draw(window)
            bullet.move()

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_d]:
            self.hitbox.x += self.speed

        if keys[pygame.K_a]:
            self.hitbox.x -= self.speed

        if keys[pygame.K_f]:
            self.patronu.append(Bullet(self.hitbox.x,self.hitbox.y,50,50,"kartka/bullet.png",10))



