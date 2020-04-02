# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 15:49:02 2020

@author: Kirti Swagat Mohanty

Library Used: OpenCV
Version: 4.2.0
Python Version: 3.7.4
"""

from cv2 import imread
from cv2 import imshow
from cv2 import imwrite
from cv2 import waitKey
from cv2 import destroyAllWindows

image= imread('kirti.jpg')
imwrite('new_image.jpg',image)
imshow('Test Image',image)
waitKey(0)
destroyAllWindows()
