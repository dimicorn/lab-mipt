import pygame
from pygame.draw import *

pygame.init()
FPS = 30

screen = pygame.display.set_mode((600, 700))

almost_black = (1, 1, 1)

def background_color():
#this function colors the background
    sky_blue = (0, 255, 247)
    grass_green = (0, 255, 0)
    rect(screen, sky_blue, (0, 0, 600, 350))
    rect(screen, grass_green, (0, 350, 600, 350))

background_color()

def sun(x, y, r):
#function that draws a sun on sun_surface with gradient,
#where x,y are coordinates of the sun, r is the radius of the sun
    yellow = (255, 230, 80)
    black = (0, 0, 0)
    for i in range (r):
        sun_surface = pygame.Surface((600, 700))
        circle(sun_surface, yellow, (x, y), r - i)
        sun_surface.set_alpha(10 + 0,5*i)
        sun_surface.set_colorkey(black)
        screen.blit(sun_surface, (0, 0))
        
sun(500, 160, 85)

def tree(x, y, k):
#function that draws a tree on surface "screen" using a rect and multiple ellipse functions,
#where x,y are coordinates of the tree and k - size coefficient
    white = (255, 255, 255)
    tree_green1 = (0, 150, 10)
    tree_green2 = (60, 255, 0)
    pink = (255, 190, 230)
    rect(screen, white, (x, y, 30*k, 200*k))
    ellipse(screen, tree_green1,[x - 125*k, y - 105*k, 300*k, 143*k], 0)
    ellipse(screen, tree_green2,[x - 125*k, y - 105*k, 300*k, 143*k], 6)
    ellipse(screen, tree_green1,[x - 63*k, y - 265*k, 165*k, 210*k], 0)
    ellipse(screen, tree_green2,[x - 63*k, y - 265*k, 165*k, 210*k], 6)
    ellipse(screen, tree_green1,[x - 63*k, y - 35*k, 165*k, 120*k], 0)
    ellipse(screen, tree_green2,[x - 63*k, y - 35*k, 165*k, 120*k], 6)
    ellipse(screen, pink,[x - 30*k, y - 195*k, 45*k, 38*k], 0)
    ellipse(screen, pink,[x + 95*k, y - 65*k, 45*k, 38*k], 0)
    ellipse(screen, pink,[x - 90*k, y - 70*k, 45*k, 38*k], 0)
    ellipse(screen, pink,[x + 20*k, y + 25*k, 45*k, 38*k], 0)
    
tree(120, 225, 1)
tree(40, 325, 0.7)
tree(100, 490, 0.4)

#creating a surface for unicorns
unicorn_surface = pygame.Surface((600, 700))
rect(unicorn_surface, almost_black, (0, 0, 600, 700))
unicorn_surface.set_colorkey(almost_black)

def unicorn(x, y, k):
#function that draws a unicorn on unicorn_surface using multiple different functions,
#where x,y are coordinates of the unicorn and k - size coefficient

#this part draws unicorn's body
    white = (255, 255, 255)
    black = (0, 0, 0)
    pink1 = (255, 115, 220)
    pink2 = (255, 150, 255)
    blue = (150, 255, 255)
    yellow = (255, 255, 80)
    ellipse(unicorn_surface, white,[x, y, 150*k, 60*k], 0)
    
#this draws neck and head
    rect(unicorn_surface, white, (x + 100*k, y - 60*k, 35*k, 75*k))
    ellipse(unicorn_surface, white, [x + 95*k, y - 65*k, 80*k, 30*k])
    ellipse(unicorn_surface, white, [x + 100*k, y - 75*k, 50*k, 50*k])
    polygon(unicorn_surface, pink1, ([x + 115*k, y - 75*k], [x + 130*k, y - 73*k],
                                    [x + 128*k, y - 130*k]))
#this draws legs
    rect(unicorn_surface, white, (x + 20*k, y + 50*k, 13*k, 50*k))
    rect(unicorn_surface, white, (x + 40*k, y + 50*k, 13*k, 58*k))
    rect(unicorn_surface, white, (x + 90*k, y + 50*k, 13*k, 50*k))
    rect(unicorn_surface, white, (x + 110*k, y + 50*k, 13*k, 58*k))
#this draws eyes
    ellipse(unicorn_surface, pink1, [x + 128*k, y - 60*k, 15*k, 12*k])
    ellipse(unicorn_surface, black, [x + 136*k, y - 54*k, 6*k, 5*k])
    polygon(unicorn_surface, white, ([x + 138*k, y - 55*k], [x + 136*k, y - 53*k],
                                    [x + 133*k, y - 56*k], [x + 134*k, y - 58*k]))
#this draws the mane
    ellipse(unicorn_surface, pink2, [x + 95*k, y - 80*k, 30*k, 12*k])
    ellipse(unicorn_surface, blue, [x + 93*k, y - 73*k, 30*k, 12*k])
    ellipse(unicorn_surface, yellow, [x + 85*k, y - 68*k, 30*k, 12*k])
    ellipse(unicorn_surface, pink2, [x + 81*k, y -61*k, 30*k, 12*k])
    ellipse(unicorn_surface, pink2, [x + 79*k, y - 54*k, 40*k, 20*k])
    ellipse(unicorn_surface, yellow, [x + 77*k, y - 47*k, 38*k, 12*k])
    ellipse(unicorn_surface, yellow, [x + 80*k, y - 40*k, 35*k, 25*k])
    ellipse(unicorn_surface, blue, [x + 73*k, y - 33*k, 38*k, 12*k])
    ellipse(unicorn_surface, blue, [x + 68*k, y - 26*k, 45*k, 18*k])
    ellipse(unicorn_surface, pink2, [x + 69*k, y - 19*k, 30*k, 12*k])
    ellipse(unicorn_surface, yellow, [x + 67*k, y - 12*k, 40*k, 20*k])
    
#this draws the tail
    ellipse(unicorn_surface, pink2, [x, y, 30*k, 12*k])
    ellipse(unicorn_surface, blue, [x - 2*k, y + 7*k, 30*k, 12*k])
    ellipse(unicorn_surface, yellow, [x - 10*k, y + 12*k, 30*k, 12*k])
    ellipse(unicorn_surface, pink2, [x - 14*k, y + 19*k, 30*k, 12*k])
    ellipse(unicorn_surface, pink2, [x - 16*k, y + 16*k, 40*k, 20*k])
    ellipse(unicorn_surface, yellow, [x - 18*k, y + 33*k, 38*k, 12*k])
    ellipse(unicorn_surface, yellow, [x - 15*k, y + 40*k, 35*k, 25*k])
    ellipse(unicorn_surface, blue, [x - 22*k, y + 47*k, 38*k, 12*k])
    ellipse(unicorn_surface, blue, [x - 28*k, y + 54*k, 45*k, 18*k])
    ellipse(unicorn_surface, pink2, [x - 26*k, y + 61*k, 30*k, 12*k])
    ellipse(unicorn_surface, yellow, [x - 28*k, y + 68*k, 40*k, 20*k])

def unicorn_flipper_shower(s, x, y):
#this function flips the unicorn_surface along y-axis, x-axis or just shows the unicorn on the screen
    s = pygame.transform.flip(s, x, y)
    screen.blit(s, (0,0))

def unicorn_deleter(s):
#this function colors unicorn_surface with almost_almost_black, so flipping next unicorn would be possible
    almost_almost_black = (2, 2, 2)
    rect(s, almost_almost_black, (0, 0, 600, 700))
    s.set_colorkey(almost_almost_black)
    
unicorn (200, 400, 1)
unicorn_flipper_shower(unicorn_surface, 1, 0)
unicorn_deleter(unicorn_surface)
unicorn(420, 510, 0.7)
unicorn_flipper_shower(unicorn_surface, 0, 0)

pygame.display.update()
                                                                  
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
