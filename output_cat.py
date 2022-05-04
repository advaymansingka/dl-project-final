# use this and gmm to output mouths synced to audio from wav file

import pandas as pd
import numpy as np
import wave
import sys
import csv
import sklearn as skl
import pygame
import time
import random
from sklearn.mixture import GaussianMixture
from joblib import dump, load


with open('Advay-OAMF.csv', 'r') as f:
    data = list(csv.reader(f, delimiter=","))
 
data = np.array(data)

print("Imports Complete")

gm = load('advay_OAMF_test.joblib') 
predictions = gm.predict(data)

print(predictions[0:1000])

print("GM Predictor Loaded")


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


def image_flip(img): 
    return pygame.transform.flip(img, True, False)


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
mouth_AEIL_1 = image_flip(image_halver(mouth_AEIL_1))
mouth_AEIL_2 = image_flip(image_halver(mouth_AEIL_2))

mouth_BMP_1 = pygame.image.load(r'cat_mouths/BMP 1.png')
mouth_BMP_1 = image_flip(image_halver(mouth_BMP_1))

mouth_CDGHJKNQSTXZ_1 = pygame.image.load(r'cat_mouths/CDGHJKNQSTXZ 1.png')
mouth_CDGHJKNQSTXZ_2 = pygame.image.load(r'cat_mouths/CDGHJKNQSTXZ 2.png')
mouth_CDGHJKNQSTXZ_1 = image_flip(image_halver(mouth_CDGHJKNQSTXZ_1))
mouth_CDGHJKNQSTXZ_2 = image_flip(image_halver(mouth_CDGHJKNQSTXZ_2))

mouth_FV_1 = pygame.image.load(r'cat_mouths/FV 1.png')
mouth_FV_2 = pygame.image.load(r'cat_mouths/FV 2.png')
mouth_FV_1 = image_flip(image_halver(mouth_FV_1))
mouth_FV_2 = image_flip(image_halver(mouth_FV_2))

mouth_ORUW_1 = pygame.image.load(r'cat_mouths/ORUW 1.png')
mouth_ORUW_2 = pygame.image.load(r'cat_mouths/ORUW 2.png')
mouth_ORUW_1 = image_flip(image_halver(mouth_ORUW_1))
mouth_ORUW_2 = image_flip(image_halver(mouth_ORUW_2))

step = 0

# mout_dict = {
#     1:mouth_AEIL_1,
#     2:mouth_AEIL_2,
#     3:mouth_BMP_1,
#     4:mouth_CDGHJKNQSTXZ_1,
#     5:mouth_CDGHJKNQSTXZ_2,
#     6:mouth_FV_1,
#     7:mouth_FV_2,
#     8:mouth_ORUW_1,
#     9:mouth_ORUW_2
#     }


# advay-oamf-test
mout_dict = {
    1:mouth_ORUW_1,
    2:mouth_AEIL_1,
    3:mouth_BMP_1,
    4:mouth_CDGHJKNQSTXZ_1,
    5:mouth_FV_1
    }


# pygame.mixer.init()
# my_sound = pygame.mixer.Sound('wav_tests/Advay-OAMF.wav')
# my_sound.play()

# infinite loop
while True:
  
    # completely fill the surface object
    # with white colour
    display_surface.fill(white)
  
    # copying the image surface object
    # to the display surface object at
    # (0, 0) coordinate.
    
    display_surface.blit(cat_tail, (500, 240))
    display_surface.blit(cat_body, (270, 380))
    display_surface.blit(cat_beard, (160, 340))

    display_surface.blit(cat_ear_left, (275, 295))
    display_surface.blit(cat_ear_right, (465, 290))
    display_surface.blit(cat_head, (180, 195))
    display_surface.blit(cat_nose, (422, 470))

    mouth_to_show = mout_dict[predictions[step]+1]
    display_surface.blit(mouth_to_show, (405, 480))
  
    # Draws the surface object to the screen.  
    pygame.display.update()

    time.sleep(0.02)
    step += 1
    
pygame.mixer.music.stop()


# #     for event in pygame.event.get():
#         if event.type == QUIT:
#             pygame.quit()
#             sys.exit()
