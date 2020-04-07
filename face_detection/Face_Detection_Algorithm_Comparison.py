# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 01:52:53 2020

@author: Kirti Swagat Mohanty
"""
from mtcnn.mtcnn import MTCNN
from cv2 import imread
from cv2 import imshow
from cv2 import waitKey
from cv2 import destroyAllWindows
from cv2 import rectangle
from cv2 import imwrite
import os
import time


start=time.time()
path='C:/Users/NIC/Documents/Kirti_Swagat/AI/Face_Detection/DNN/'
image_name= 'Log_out_09_01_2020.jpg'
# load the photograph
image = imread(path+image_name)
