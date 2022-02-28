import pygame
from random import *

pygame.init()
pygame.font.init()

# seed random number generator
seed(1)
################################################################################################
#                                           VARIABLES
################################################################################################
width = 500
height = 500

screen = pygame.display.set_mode([width, height])

myfont = pygame.font.SysFont('Comic Sans MS', 20)

running = True


ticks = 0

################################################################################################
#                                           FUNCTIONS
################################################################################################

################################################################################################
#                                           MAIN LOOP
################################################################################################

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                print("pressed A")
            elif event.key == pygame.K_d:
                print("pressed D")


    ##################################################################
    # DRAW CODE
    ##################################################################
    # Fill the background with white
    screen.fill((255, 255, 255))


    textsurface = myfont.render('Ticks = ' + str(ticks), False, (0, 0, 0))
    screen.blit(textsurface, (0, 0))
    ##################################################################
    # Flip the display
    ##################################################################
    pygame.display.flip()


# Done! Time to quit.
pygame.quit()