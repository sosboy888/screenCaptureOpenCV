# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 18:20:40 2018

@author: Intal
"""

import numpy as np
import cv2
from PIL import ImageGrab
img = ImageGrab.grab(bbox=(0, 0, 1920, 1080))
img_np = np.array(img)

frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)

while True: #x, y, w, h
    img = ImageGrab.grab(bbox=(0, 0, 1920, 1080))
    img_np = np.array(img)
    frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
    cv2.imshow("frame", frame)
    cv2.waitKey(1)

cv2.destroyAllWindows() 