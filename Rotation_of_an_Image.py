# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 17:14:17 2020

@author: Kirti Swagat Mohanty
Library Used: OpenCV
Version: 4.2.0
Python Version: 3.7.4
"""

from cv2 import imread
from cv2 import imshow
from cv2 import imwrite
from cv2 import resize
from cv2 import getRotationMatrix2D,warpAffine
from cv2 import waitKey
from cv2 import destroyAllWindows

#Reading an Image
image=imread('kirti.jpg')

#Extracting the size of the image
height, width= image.shape[0:2]
print('The Height of the Image:',height)
print('The Width of the Image',width)

rotation_matrix= getRotationMatrix2D((width/2,height/2,),32,1)
rotated_image = warpAffine(image, rotation_matrix, (width, height))

#Resizing the Image
image=resize(image,(600,400))
imshow('original image',image)
rotated_image=resize(rotated_image,(600,400))
imshow('Rotated image',rotated_image)
imwrite('Rotated_image.jpg',rotated_image)


waitKey(0)
destroyAllWindows()

