#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
number = random.randint(1,20)
print(number)


# In[ ]:





# In[ ]:


import pygame
import time

pygame.init()
cnavas = pygame.display.set_mode((500,500))


# In[1]:


import pygame ,sys ,time
from sys import exit
from pygame.locals import *
pygame.init()
DISPLAY_SURF = pygame.display.set_mode((500,500),0,32)

BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN  = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)

DISPLAY_SURF.fill(WHITE)

pygame.draw.polygon(DISPLAY_SURF, GREEN, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))
pygame.draw.circle(DISPLAY_SURF ,RED ,(250,250),50,10)
pygame.draw.line(DISPLAY_SURF , BLUE ,(0,0),(250,250),)



while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.display.quit()
            pygame.quit()
            sys.exit   
        pygame.display.update()

