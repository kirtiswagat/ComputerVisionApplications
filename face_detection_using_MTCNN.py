# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 13:17:38 2020

@author: NIC
"""

from mtcnn.mtcnn import MTCNN
from cv2 import imread
from cv2 import imshow
from cv2 import waitKey
from cv2 import destroyAllWindows
from cv2 import rectangle
from cv2 import imwrite
import os




path='C:/Users/NIC/Documents/Kirti_Swagat/AI/Face_Detection/PJ-4_2863_SIEMANL_004_BSC_Q0601_000011/Logout/'
image_name= 'Log_out_04_01_2020.jpg'
# load the photograph
image = imread(path+image_name)




'''
#Face Detection Using MTCNN
'''
detector = MTCNN()
# detect faces in the image
faces = detector.detect_faces(image)
#print("Number of Faces Detected:",len(faces))
for i in range(len(faces)):
    #print(len(faces))
    x,y,width,height=faces[i]['box']
    x2,y2= x+width, y+height
    rectangle(image, (x,y), (x2,y2),(0,0,255),1)
    #sub_faces=image[y:y2,x:x2]
    #face_file_name="faces/face_"+str(y)+".jpg"
    #imwrite(face_file_name,sub_faces)

#imshow('face detection', image)
imwrite("./MTCNN/" + image_name,image)
file_name= os.path.splitext(image_name)[0]
output_result= open("./MTCNN/"+"MTCNN_Result_" + str(file_name) + ".txt", "w")
output_result.write("No of Faces Detected Using MTCNN Method for the image named "+str(file_name)+":"+str(len(faces)))
output_result.close()
waitKey(0)
destroyAllWindows()

