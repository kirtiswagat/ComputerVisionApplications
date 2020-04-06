# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 20:18:41 2020

@author: Kirti Swagat Mohanty
@Description: Copying Odd numbered Images from a folder to another folder
"""

import os
import re
import shutil

base_dir= os.path.dirname(__file__)
pattern = re.compile(r"[a-zA-Z]+(\d+)\.[a-zA-Z]+")
input_directory_name= os.path.join(base_dir+'/all_images/')
output_directory_name= os.path.join(base_dir+'/faces/')
print(output_directory_name)


for file in os.listdir(base_dir+'/all_images/'):
    
    if int(re.search(pattern, file).group(1))%2 != 0:
        shutil.copy(input_directory_name+ file, output_directory_name)
        print(f"copying odd numbered file {file} to "+str(output_directory_name))
    else:
        print(f"skipping even numbered file {file}")
