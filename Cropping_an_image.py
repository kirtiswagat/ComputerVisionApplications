# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 18:03:16 2020

@author: Kirti Swagat Mohanty
Library Used: OpenCV
Version: 4.2.0
Python Version: 3.7.4
"""

from cv2 import imread
from cv2 import imshow
from cv2 import imwrite
from cv2 import resize
from cv2 import waitKey
from cv2 import destroyAllWindows

#Reading an Image
image=imread('kirti.jpg')

#Extracting the size of the image
height, width= image.shape[0:2]
print('The Height of the Image:',height)
print('The Width of the Image',width)

height_start=int(height*.40)
height_end=int(height*.80)

width_start=int(width*.50)
width_end=int(width*.90)

cropped_image=image[height_start:height_end, width_start:width_end]
imwrite('cropped_image.jpg',cropped_image)
cropped_image=resize(cropped_image,(600,400))
imshow('Cropped Image',cropped_image)

waitKey(0)
destroyAllWindows()
