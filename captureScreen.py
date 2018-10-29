# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 18:20:40 2018

@author: sosboy888
"""

import numpy as np
import cv2
from PIL import ImageGrab
#specify the resolution of your window below along with the top right corner of the box, here we will consider the top right corner as 0,0 consider the whole screen.
img = ImageGrab.grab(bbox=(0, 0, 1920, 1080)) #boxX,boxY,w,h
img_np = np.array(img)
#creating a frame using a numpy array
frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)

while True: 
    #same function repeated below
    img = ImageGrab.grab(bbox=(0, 0, 1920, 1080))
    img_np = np.array(img)
    frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
    #used to show and update the opencv window
    cv2.imshow("frame", frame)
    cv2.waitKey(1)

cv2.destroyAllWindows() 
