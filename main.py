import pygame
from pygame import *
from Rocket import Rocket
from NLO import NLO


window = pygame.display.set_mode((700,500))
fps = pygame.time.Clock()

backround = pygame.transform.scale(
    pygame.image.load("kartka/galaxy.jpg"),(700,500)
)

rocket = Rocket(300,390,100,100, "kartka/rocket.png",10)

nlo1 = []
nlo1.append(NLO(360,100,80,50, "kartka/ufo.png",10))
nlo1.append(NLO(400,100,80,50, "kartka/ufo.png",10))







game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())







    window.blit(backround, (0, 0))
    for nlo in nlo1:
        nlo.draw(window)
    rocket.move()
    rocket.draw(window)
    pygame.display.flip()
    fps.tick(60)