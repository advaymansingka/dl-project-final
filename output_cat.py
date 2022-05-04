# use this and gmm to output mouths synced to audio from wav file

import pandas as pd
import numpy as np
import wave
import sys
import csv
import sklearn as skl
import pygame


np.array([1,2,3,1,2,3])

# activate the pygame library .
# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()
  
# define the RGB value
# for white colour
white = (255, 255, 255)
  
# assigning values to X and Y variable
X = 1000
Y = 1000
  
# create the display surface object
# of specific dimension..e(X, Y).
display_surface = pygame.display.set_mode((X, Y ))
  
# set the pygame window name
pygame.display.set_caption('Image')
  

def image_halver(img, scaling=0.5):
    height = scaling * img.get_height()
    width = scaling * img.get_width()
    i = pygame.transform.scale(img,(width,height))
    return i


# create a surface object, image is drawn on it.
cat_beard = pygame.image.load(r'cat_parts/Cat Beard 1.png')
cat_beard = image_halver(cat_beard)

cat_head = pygame.image.load(r'cat_parts/Cat Head.png')
cat_head = image_halver(cat_head)

cat_ear_left = pygame.image.load(r'cat_parts/Cat Ear Left.png')
cat_ear_left = image_halver(cat_ear_left)

cat_ear_right = pygame.image.load(r'cat_parts/Cat Ear Right.png')
cat_ear_right = image_halver(cat_ear_right)

cat_nose = pygame.image.load(r'cat_parts/Cat Nose.png')
cat_nose = image_halver(cat_nose)

cat_body = pygame.image.load(r'cat_parts/Cat Body.png')
cat_body = image_halver(cat_body)

cat_tail = pygame.image.load(r'cat_parts/Cat Tail 1.png')
cat_tail = image_halver(cat_tail)

mouth_AEIL_1 = pygame.image.load(r'cat_mouths/AEIL 1.png')
mouth_AEIL_2 = pygame.image.load(r'cat_mouths/AEIL 1.png')
mouth_AEIL_1 = image_halver(mouth_AEIL_1)
mouth_AEIL_2 = image_halver(mouth_AEIL_2)

mouth_BMP_1 = pygame.image.load(r'cat_mouths/BMP 1.png')
mouth_BMP_1 = image_halver(mouth_BMP_1)

mouth_CDGHJKNQSTXZ_1 = pygame.image.load(r'cat_mouths/CDGHJKNQSTXZ 1.png')
mouth_CDGHJKNQSTXZ_2 = pygame.image.load(r'cat_mouths/CDGHJKNQSTXZ 2.png')
mouth_CDGHJKNQSTXZ_1 = image_halver(mouth_CDGHJKNQSTXZ_1)
mouth_CDGHJKNQSTXZ_2 = image_halver(mouth_CDGHJKNQSTXZ_2)

mouth_FV_1 = pygame.image.load(r'cat_mouths/FV 1.png')
mouth_FV_2 = pygame.image.load(r'cat_mouths/FV 2.png')
mouth_FV_1 = image_halver(mouth_FV_1)
mouth_FV_2 = image_halver(mouth_FV_2)

mouth_ORUW_1 = pygame.image.load(r'cat_mouths/ORUW 1.png')
mouth_ORUW_2 = pygame.image.load(r'cat_mouths/ORUW 2.png')
mouth_ORUW_1 = image_halver(mouth_ORUW_1)
mouth_ORUW_2 = image_halver(mouth_ORUW_2)



# infinite loop
while True :
  
    # completely fill the surface object
    # with white colour
    display_surface.fill(white)
  
    # copying the image surface object
    # to the display surface object at
    # (0, 0) coordinate.
    
    display_surface.blit(cat_tail, (500, 300))
    display_surface.blit(cat_body, (300, 400))
    display_surface.blit(cat_beard, (200, 200))

    display_surface.blit(cat_ear_left, (200, 200))
    display_surface.blit(cat_ear_right, (400, 200))
    display_surface.blit(cat_head, (200, 200))
    display_surface.blit(cat_nose, (200, 200))
  
    # iterate over the list of Event objects
    # that was returned by pygame.event.get() method.
    for event in pygame.event.get() :
  
        # if event object type is QUIT
        # then quitting the pygame
        # and program both.
        if event.type == pygame.QUIT :
  
            # deactivates the pygame library
            pygame.quit()
  
            # quit the program.
            quit()
  
        # Draws the surface object to the screen.  
        pygame.display.update()

    