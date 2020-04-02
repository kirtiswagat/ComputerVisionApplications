# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 18:47:18 2020

@author: Kirti Swagat Mohanty
Library Used: OpenCV
Version: 4.2.0
Python Version: 3.7.4
"""

import cv2
import numpy as np

image=cv2.imread('kirti.jpg')

'''
cv2.addWeighted(source_img1, alpha1, source_img2, alpha2, beta)

source_img1= Original Image
source_img2= Synthetic Image with same size with that of the Original but filled with 0.
alpha defines contrast of the Image.
if alpha>1: there will be higher contrast
if 0<alpha<1: there will be lower contrast
if alpha=1: there will not be any changes

beta value ranges -127 to +127

'''

contrast_img= cv2.addWeighted(image,2.3,np.zeros(image.shape, image.dtype),1,0)

image=cv2.resize(image,(600,400))
cv2.imshow('Original Image',image)

contrast_img=cv2.resize(contrast_img,(600,400))
cv2.imshow('Contrast_image',contrast_img)
cv2.imwrite('Contrast_image.jpg',contrast_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
