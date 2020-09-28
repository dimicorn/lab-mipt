import pygame
from pygame.draw import *

pygame.init()
FPS=30
screen = pygame.display.set_mode((600, 700))
#background
rect(screen, (0,255,247), (0,0,600,350))
rect(screen, (0,255,0), (0,350,600,350))

for i in range (85):
    s=pygame.Surface((170,170))
    circle(s,(255,230,80), (85, 85), 85-i)
    s.set_alpha(10+0,5*i)
    s.set_colorkey((0,0,0))
    screen.blit(s, (415,75))
def tree(x,y,k):
#tree1
    rect(screen, (255,255,255), (x,y,30*k,200*k))
    ellipse(screen, (0,150,10),[x-125*k, y-105*k, 300*k, 143*k], 0)
    ellipse(screen, (60,255,0),[x-125*k, y-105*k, 300*k, 143*k], 6)
    ellipse(screen, (0,150,10),[x-63*k, y-265*k, 165*k, 210*k], 0)
    ellipse(screen, (60,255,0),[x-63*k, y-265*k, 165*k, 210*k], 6)
    ellipse(screen, (0,150,10),[x-63*k, y-35*k, 165*k, 120*k], 0)
    ellipse(screen, (60,255,0),[x-63*k, y-35*k, 165*k, 120*k], 6)
    ellipse(screen, (255,190,230),[x-30*k, y-195*k, 45*k, 38*k], 0)
    ellipse(screen, (255,190,230),[x+95*k, y-65*k, 45*k, 38*k], 0)
    ellipse(screen, (255,190,230),[x-90*k, y-70*k, 45*k, 38*k], 0)
    ellipse(screen, (255,190,230),[x+20*k, y+25*k, 45*k, 38*k], 0)
tree(120,225,1)
tree(40,325,0.7)
tree(100,490,0.4)
s=pygame.Surface((600,700))
rect(s, (1,1,1), (0,0,600,700))
s.set_colorkey((1,1,1))
def unicorn(x,y,k):
#UNICORN
    ellipse(s, (255,255,255),[x, y, 150*k, 60*k], 0) #body
    rect(s, (255,255,255), (x+100*k, y-60*k, 35*k, 75*k))#neck and head
    ellipse(s, (255,255,255), [x+95*k, y-65*k, 80*k, 30*k])
    ellipse(s, (255,255,255), [x+100*k, y-75*k, 50*k, 50*k])
    polygon(s, (255,115,220), ([x+115*k,y-75*k], [x+130*k,y-73*k],
                                    [x+128*k, y-130*k]))
    rect(s, (255,255,255), (x+20*k, y+50*k, 13*k, 50*k)) #legs
    rect(s, (255,255,255), (x+40*k, y+50*k, 13*k, 58*k))
    rect(s, (255,255,255), (x+90*k, y+50*k, 13*k, 50*k))
    rect(s, (255,255,255), (x+110*k, y+50*k, 13*k, 58*k))
#eye
    ellipse(s, (255,115,220), [x+128*k, y-60*k, 15*k,12*k])
    ellipse(s, (0,0,0), [x+136*k, y-54*k, 6*k,5*k])
    polygon(s, (255,255,255), ([x+138*k,y-55*k], [x+136*k,y-53*k],
                                    [x+133*k,y-56*k], [x+134*k, y-58*k]))
#hair
    ellipse(s, (255,150,255), [x+95*k, y-80*k, 30*k,12*k]) #pink
    ellipse(s, (150,255,255), [x+93*k, y-73*k, 30*k,12*k]) #blue
    ellipse(s, (255,255,80), [x+85*k, y-68*k, 30*k,12*k])  #yellow
    ellipse(s, (255,150,255), [x+81*k, y-61*k, 30*k,12*k])
    ellipse(s, (255,150,255), [x+79*k, y-54*k, 40*k,20*k])
    ellipse(s, (255,255,80), [x+77*k, y-47*k, 38*k, 12*k])
    ellipse(s, (255,255,80), [x+80*k, y-40*k, 35*k,25*k])
    ellipse(s, (150,255,255), [x+73*k, y-33*k, 38*k,12*k])
    ellipse(s, (150,255,255), [x+68*k, y-26*k, 45*k,18*k])
    ellipse(s, (255,150,255), [x+69*k, y-19*k, 30*k,12*k])
    ellipse(s, (255,255,80), [x+67*k, y-12*k, 40*k,20*k])
#tail
    ellipse(s, (255,150,255), [x, y, 30*k,12*k]) #pink
    ellipse(s, (150,255,255), [x-2*k, y+7*k, 30*k,12*k]) #blue
    ellipse(s, (255,255,80), [x-10*k, y+12*k, 30*k,12*k])#yellow
    ellipse(s, (255,150,255), [x-14*k, y+19*k, 30*k,12*k])
    ellipse(s, (255,150,255), [x-16*k, y+16*k, 40*k,20*k])
    ellipse(s, (255,255,80), [x-18*k, y+33*k, 38*k, 12*k])
    ellipse(s, (255,255,80), [x-15*k, y+40*k, 35*k,25*k])
    ellipse(s, (150,255,255), [x-22*k, y+47*k, 38*k,12*k])
    ellipse(s, (150,255,255), [x-28*k, y+54*k, 45*k,18*k])
    ellipse(s, (255,150,255), [x-26*k, y+61*k, 30*k,12*k])
    ellipse(s, (255,255,80), [x-28*k, y+68*k, 40*k,20*k])
unicorn (200,400,1)
l=pygame.Surface((600,700))
l=pygame.transform.flip(s, 1, 0)
rect(s, (2,2,2), (0,0,600, 700))
s.set_colorkey((2,2,2))
screen.blit(l, (0,0))



unicorn(420,510, 0.7)
pygame.transform.flip(screen,True, False)
screen.blit(s, (0,0))

pygame.display.update()
                                                                  
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
