# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 11:41:46 2020

@author: Kirti Swagat Mohanty
"""
import os
import re
import cv2
import time
import face_recognition
from mtcnn.mtcnn import MTCNN

start_time_overall= time.time()

base_dir= os.path.dirname(__file__)
pattern = re.compile(r"[a-zA-Z]+(\d+)\.[a-zA-Z]+")

input_directory_name= os.path.join(base_dir+'/all_images/')
output_directory_name= os.path.join(base_dir+'/faces/')

count=0
for file in os.listdir(base_dir+'/all_images/'):
    image= cv2.imread(input_directory_name+file)
    
    #Haar Cascade Based Face Detection Start
    start_time_Haar= time.time()
    detector= cv2.CascadeClassifier('C:/Users/NIC/Documents/Kirti_Swagat/AI/Face_Detection/haarcascade_frontalface_default.xml')
    faces= detector.detectMultiScale(image, 1.3, 5)
    for face in faces:
        x,y,width, height=face
        x2,y2= x+width, y+height
        cv2.rectangle(image, (x,y), (x2,y2),(255,0,0),2)
    cv2.imwrite("C:/Users/NIC/Documents/Kirti_Swagat/AI/Face_Detection/faces/Haar/"+file,image)
    cv2.putText(image,str(len(faces)),(20,20),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0,),2)
    output_result=open("C:/Users/NIC/Documents/Kirti_Swagat/AI/Face_Detection/faces/Haar.txt","a")
    output_result.write("No of Faces Detected Using HARR Method for the image named "+str(file)+":"+str(len(faces)))
    output_result.write(os.linesep)
    end_time_Haar=time.time()
    print("Execution Time (in seconds) for Haar based Face Detection :", format(end_time_Haar - start_time_Haar, '.2f'))
    #Haar Cascade Based Face Detection End
    
    #HOG Based Face Detection Start
    start_time_HOG= time.time()
    faces_HOG = face_recognition.face_locations(image)
    
    for (top, right, bottom, left) in faces_HOG:
        cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0),2)
    cv2.imwrite("C:/Users/NIC/Documents/Kirti_Swagat/AI/Face_Detection/faces/HOG/"+file,image)
    cv2.putText(image,str(len(faces_HOG)),(60,60),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0,),2)
    output_result=open("C:/Users/NIC/Documents/Kirti_Swagat/AI/Face_Detection/faces/HOG.txt","a")
    output_result.write("No of Faces Detected Using HOG Method for the image named "+str(file)+":"+str(len(faces_HOG)))
    output_result.write(os.linesep)
    end_time_HOG= time.time()
    print("Execution Time (in seconds) for HOG based Face Detection :", format(end_time_HOG - start_time_HOG, '.2f'))
    #HOG Based Face Detection End
    
    #MTCNN Based Face Detection Start
    start_time_MTCNN= time.time()
    detector= MTCNN()
    faces_MTCNN=detector.detect_faces(image)
    for i in range(len(faces_MTCNN)):
        x,y,width,height=faces_MTCNN[i]['box']
        x2,y2= x+width, y+height
        cv2.rectangle(image, (x,y), (x2,y2),(0,0,255),2)
    cv2.imwrite("C:/Users/NIC/Documents/Kirti_Swagat/AI/Face_Detection/faces/MTCNN/"+file,image)
    cv2.putText(image,str(len(faces_MTCNN)),(80,80),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255,),2)
    output_result=open("C:/Users/NIC/Documents/Kirti_Swagat/AI/Face_Detection/faces/MTCNN.txt","a")
    output_result.write("No of Faces Detected Using MTCNN Method for the image named "+str(file)+":"+str(len(faces_MTCNN)))
    output_result.write(os.linesep)
    end_time_MTCNN= time.time()
    print("Execution Time (in seconds) for MTCNN based Face Detection :", format(end_time_MTCNN - start_time_MTCNN, '.2f'))
    #MTCNN Based Face Detection End
    
    
    
    
    
    
end_time_overall= time.time()
print("Execution Time (in seconds) for Comparison for Face Detection :", format(end_time_overall - start_time_overall, '.2f'))
