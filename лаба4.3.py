import pygame
from pygame.draw import *

pygame.init()
FPS=30
screen = pygame.display.set_mode((600, 700))
#background
rect(screen, (0,255,247), (0,0,600,350))
rect(screen, (0,255,0), (0,350,600,350))
circle(screen, (255,230,80), (500,75), 85)
#tree1
rect(screen, (255,255,255), (120,225,30,200))
ellipse(screen, (0,150,10),[-5, 120, 300, 143], 0)
ellipse(screen, (60,255,0),[-5, 120, 300, 143], 6)
ellipse(screen, (0,150,10),[57, -40, 165, 210], 0)
ellipse(screen, (60,255,0),[57, -40, 165, 210], 6)
ellipse(screen, (0,150,10),[57, 190, 165, 120], 0)
ellipse(screen, (60,255,0),[57, 190, 165, 120], 6)
ellipse(screen, (255,190,230),[150, 30, 45, 38], 0)
ellipse(screen, (255,190,230),[215, 160, 45, 38], 0)
ellipse(screen, (255,190,230),[30, 155, 45, 38], 0)
ellipse(screen, (255,190,230),[140, 250, 45, 38], 0)
#tree2
rect(screen, (255,255,255), (40,325,40,200))
ellipse(screen, (0,150,10),[-35, 320, 200, 95], 0)
ellipse(screen, (60,255,0),[-35, 320, 200, 95], 6)
ellipse(screen, (0,150,10),[5, 230, 110, 140], 0)
ellipse(screen, (60,255,0),[5, 230, 110, 140], 6)
ellipse(screen, (0,150,10),[5, 390, 110, 80], 0)
ellipse(screen, (60,255,0),[5, 390, 110, 80], 6)
ellipse(screen, (255,190,230),[70, 270, 30, 25], 0)
ellipse(screen, (255,190,230),[115, 360, 30, 25], 0)
ellipse(screen, (255,190,230),[-10, 355, 30, 25], 0)
ellipse(screen, (255,190,230),[70, 430, 30, 25], 0)
#tree3
rect(screen, (255,255,255), (100,490,20,220))
ellipse(screen, (0,150,10),[25, 525, 160, 95], 0)
ellipse(screen, (60,255,0),[25, 525, 160, 95], 6)
ellipse(screen, (0,150,10),[65, 435, 88, 140], 0)
ellipse(screen, (60,255,0),[65, 435, 88, 140], 6)
ellipse(screen, (0,150,10),[65, 595, 88, 80], 0)
ellipse(screen, (60,255,0),[65, 595, 88, 80], 6)
ellipse(screen, (255,190,230),[100, 475, 24, 20], 0)
ellipse(screen, (255,190,230),[145, 565, 24, 20], 0)
ellipse(screen, (255,190,230),[50, 560, 24, 20], 0)
ellipse(screen, (255,190,230),[100, 635, 24, 20], 0)
#UNICORN
ellipse(screen, (255,255,255),[200, 400, 150, 60], 0) #body
rect(screen, (255,255,255), (300, 340, 35, 75))   #neck and head
ellipse(screen, (255,255,255), [295, 335, 80, 30])
ellipse(screen, (255,255,255), [300, 325, 50, 50])
polygon(screen, (255,115,220), ([315,325], [330,327], [328, 270]))
rect(screen, (255,255,255), (220, 450, 13, 50)) #legs
rect(screen, (255,255,255), (240, 450, 13, 58))
rect(screen, (255,255,255), (290, 450, 13, 50))
rect(screen, (255,255,255), (310, 450, 13, 58))
#eye
ellipse(screen, (255,115,220), [328, 340, 15,12])
ellipse(screen, (0,0,0), [336, 344, 6,5])
polygon(screen, (255,255,255), ([338,345], [336,347], [333,344], [334, 342]))
#hair
ellipse(screen, (255,150,255), [295, 320, 30,12]) #pink
ellipse(screen, (150,255,255), [293, 327, 30,12]) #blue
ellipse(screen, (255,255,80), [285, 332, 30,12])  #yellow
ellipse(screen, (255,150,255), [281, 339, 30,12])
ellipse(screen, (255,150,255), [279, 346, 40,20])
ellipse(screen, (255,255,80), [277, 353, 38, 12])
ellipse(screen, (255,255,80), [280, 360, 35,25])
ellipse(screen, (150,255,255), [273, 367, 38,12])
ellipse(screen, (150,255,255), [268, 374, 45,18])
ellipse(screen, (255,150,255), [269, 381, 30,12])
ellipse(screen, (255,255,80), [267, 388, 40,20])
#tail
ellipse(screen, (255,150,255), [200, 400, 30,12]) #pink
ellipse(screen, (150,255,255), [198, 407, 30,12]) #blue
ellipse(screen, (255,255,80), [190, 412, 30,12])  #yellow
ellipse(screen, (255,150,255), [186, 419, 30,12])
ellipse(screen, (255,150,255), [184, 416, 40,20])
ellipse(screen, (255,255,80), [182, 433, 38, 12])
ellipse(screen, (255,255,80), [185, 440, 35,25])
ellipse(screen, (150,255,255), [178, 447, 38,12])
ellipse(screen, (150,255,255), [172, 454, 45,18])
ellipse(screen, (255,150,255), [174, 461, 30,12])
ellipse(screen, (255,255,80), [172, 468, 40,20])

#UNICORN2
ellipse(screen, (255,255,255),[420, 510, 150, 60], 0) #body
rect(screen, (255,255,255), (440, 560, 13, 50)) #legs
rect(screen, (255,255,255), (460, 560, 13, 58))
rect(screen, (255,255,255), (510, 560, 13, 50))
rect(screen, (255,255,255), (530, 560, 13, 58))
rect(screen, (255,255,255), (430, 460, 30, 75))   #neck and head
ellipse(screen, (255,255,255), [385, 450, 80, 30])
ellipse(screen, (255,255,255), [412, 438, 50, 50])
polygon(screen, (255,115,220), ([423,443], [438,440], [425, 385]))
ellipse(screen, (255,115,220), [420, 450, 15,12])
#eye
ellipse(screen, (0,0,0), [422, 454, 6,5])
polygon(screen, (255,255,255), ([425,455], [429,452], [430,454], [427, 456]))
#hair
ellipse(screen, (255,150,255), [435, 435, 30,12]) #pink
ellipse(screen, (150,255,255), [437, 442, 30,12]) #blue
ellipse(screen, (255,255,80), [445, 447, 30,12])  #yellow
ellipse(screen, (255,150,255), [449, 454, 30,12])
ellipse(screen, (255,150,255), [446, 461, 40,20])
ellipse(screen, (255,255,80), [450, 468, 38, 12])
ellipse(screen, (255,255,80), [452, 475, 35,25])
ellipse(screen, (150,255,255), [453, 482, 38,12])
ellipse(screen, (150,255,255), [454, 489, 45,18])
ellipse(screen, (255,150,255), [457, 496, 30,12])
ellipse(screen, (255,255,80), [458, 502, 40,20])
#tail
ellipse(screen, (255,150,255), [530, 515, 30,12]) #pink
ellipse(screen, (150,255,255), [532, 522, 30,12]) #blue
ellipse(screen, (255,255,80), [540, 527, 30,12])  #yellow
ellipse(screen, (255,150,255), [544, 534, 30,12])
ellipse(screen, (255,150,255), [541, 541, 40,20])
ellipse(screen, (255,255,80), [545, 548, 38, 12])
ellipse(screen, (255,255,80), [547, 555, 35,25])
ellipse(screen, (150,255,255), [548, 562, 38,12])
ellipse(screen, (150,255,255), [549, 569, 45,18])
ellipse(screen, (255,150,255), [552, 576, 30,12])
ellipse(screen, (255,255,80), [553, 582, 40,20])

pygame.display.update()
                                                                  
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
