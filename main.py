import math
import pygame
from random import *

from player import Player

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

actual_player = Player((width / 2, height / 2))
move_increment = 10
orientation_increment = math.pi / 16
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
            if event.key == pygame.K_w:
                actual_player.apply_veclocity_mag(2)
            elif event.key == pygame.K_s:
                actual_player.apply_veclocity_mag(-2)

            #TODO: IMPLEMENT ROTATION
            if event.key == pygame.K_q:
                actual_player.orientation -= orientation_increment
            elif event.key == pygame.K_e:
                actual_player.orientation += orientation_increment

            if event.key == pygame.K_SPACE:
                #TODO: MAYBE CATCH MINERAL
                pass
            if event.key == pygame.K_f:
                #TODO: MAYBE ATTACK
                pass


    ##################################################################
    # DRAW CODE
    ##################################################################
    # Fill the background with white
    screen.fill((255, 255, 255))

    actual_player.draw(screen)

    textsurface = myfont.render('Ticks = ' + str(ticks), False, (0, 0, 0))
    screen.blit(textsurface, (0, 0))
    ##################################################################
    # Flip the display
    ##################################################################
    pygame.display.flip()


# Done! Time to quit.
pygame.quit()