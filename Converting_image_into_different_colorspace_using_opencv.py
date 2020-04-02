# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 16:09:35 2020

@author: Kirti Swagat Mohanty
Library Used: OpenCV
Version: 4.2.0
Python Version: 3.7.4
"""

from cv2 import imread
from cv2 import imshow
from cv2 import imwrite
from cv2 import cvtColor
from cv2 import COLOR_BGR2GRAY,COLOR_BGR2HSV
from cv2 import resize
from cv2 import waitKey
from cv2 import destroyAllWindows

image= imread('kirti.jpg')
#converting image to Gray scale 
gray_image = cvtColor(image,COLOR_BGR2GRAY)
#Resizing the Image
resized_gray_image=resize(gray_image, (600, 400))
#Saving the Image to the Drive
imwrite('new_gray_image.jpg',gray_image)
#Showing/Displaying the Image
imshow('Gray Image',resized_gray_image)

#Converting Image into HSV Plane
hsv_image = cvtColor(image,COLOR_BGR2HSV)
#Resizing the HSV Image
resized_hsv_image=resize(hsv_image, (600, 400))
#Showing/Displaying the Image
imshow('HSV Image',resized_hsv_image)
#Storing the HSV Image to Drive
imwrite('new_hsv_image.jpg',hsv_image)

waitKey(0)
destroyAllWindows()