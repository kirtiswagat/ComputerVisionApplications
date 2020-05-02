# -*- coding: utf-8 -*-
"""
Created on Sat May  2 20:11:49 2020

@author: Kirti Swagat Mohanty
"""
import os
import pandas as pd
from shutil import copyfile
import re

image_path_csv= 'F:/Kirti_Swagat/AI/COVID_19_Predictions/Kirti_training_on_Covid/ResNet50/stage_2_detailed_class_info.csv'

csv_resnet = pd.read_csv(image_path_csv, nrows=None)
index_id= csv_resnet.type =="Normal"
types= ['Normal']
csv_indx_keep = csv_resnet.type.isin(types)

new_csv= csv_resnet[csv_indx_keep]

new_csv= new_csv.reset_index(drop=True)

patients=[]

for index,row in new_csv.iterrows():
    if row['type']== 'Normal':
        patients.append(row['patientId'])
        
new_image_path= 'F:/Kirti_Swagat/AI/COVID_19_Predictions/Kirti_training_on_Covid/ResNet50/stage_2_train_jpg/'
new_image_destination= 'F:/Kirti_Swagat/AI/COVID_19_Predictions/Kirti_training_on_Covid/ResNet50/Normal_image/'

for filename in patients:
    image_name= filename+'.jpg'
    shutil.copy(new_image_path+ image_name, new_image_destination)
    print(image_name)