# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 15:41:51 2020

@author: Kirti Swagat Mohanty
"""

from cv2 import imread
from cv2 import imshow
from cv2 import waitKey
from cv2 import destroyAllWindows
from cv2 import rectangle
from cv2 import imwrite
from cv2 import CascadeClassifier
import os

path='C:/Users/Documents/Kirti_Swagat/AI/Face_Detection/'
image_name= 'image.jpg'
# load the photograph
image = imread(path+image_name)

detector = CascadeClassifier('C:/Users/Documents/Kirti_Swagat/AI/Face_Detection/haarcascade_frontalface_default.xml')

faces= detector.detectMultiScale(image, 1.3, 5)

for face in faces:
    x,y,width, height=face
    x2,y2= x+width, y+height
    rectangle(image, (x,y), (x2,y2),(255,0,0),2)

imwrite("./HARR/" + image_name,image)
file_name= os.path.splitext(image_name)[0]
output_result= open("./HARR/"+"HARR_Result_" + str(file_name) + ".txt", "w")
output_result.write("No of Faces Detected Using HARR Method for the image named "+str(file_name)+":"+str(len(faces)))
output_result.close()
