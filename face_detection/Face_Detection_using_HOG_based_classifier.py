# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 22:17:09 2020

@author: Kirti Swagat Mohanty
"""

import face_recognition
from cv2 import imread
from cv2 import waitKey
from cv2 import destroyAllWindows
from cv2 import rectangle
from cv2 import imwrite
from cv2 import imshow
import os


path='C:/Users/Documents/Kirti_Swagat/AI/Face_Detection/'
image_name= 'image.jpg'
# load the photograph
image = imread(path+image_name)

faces = face_recognition.face_locations(image)

for (top, right, bottom, left) in faces:
    rectangle(image, (left, top), (right, bottom), (0, 255, 0),2)

imwrite("./HOG/" + image_name,image)
file_name= os.path.splitext(image_name)[0]
output_result= open("./HOG/"+"HOG_Result_" + str(file_name) + ".txt", "w")
output_result.write("No of Faces Detected Using HOG Method for the image named "+str(file_name)+":"+str(len(faces)))
output_result.close()
     
#imshow('Face Detection',image)
waitKey(0)
destroyAllWindows()
