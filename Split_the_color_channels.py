# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 16:33:37 2020

@author: Kirti Swagat Mohanty
Library Used: OpenCV
Version: 4.2.0
Python Version: 3.7.4
"""

from cv2 import imread
from cv2 import imshow
from cv2 import imwrite
from cv2 import split
from cv2 import resize
from cv2 import waitKey
from cv2 import destroyAllWindows

#Reading the Image
image= imread('kirti.jpg')

#Spliting the Color Channels
blue,green, red= split(image)


#Resising the Blue Channel Image
resized_blue_image=resize(blue, (600, 400))
#Showing/Displaying the Blue Channel Image
imshow('Blue Image',resized_blue_image)
#Saving the Blue Channel Image
imwrite('Blue_image.jpg',resized_blue_image)

#Resizing the Green Channel Image
resized_green_image=resize(green, (600, 400))
imshow('Green Image',resized_green_image)
imwrite('Green_image.jpg',resized_green_image)

#Resizing the Red Channel Image
resized_red_image=resize(red, (600, 400))
imshow('Red Image',resized_red_image)
imwrite('Red_image.jpg',resized_red_image)

waitKey(0)
destroyAllWindows()