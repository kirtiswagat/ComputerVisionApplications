import cv2
import glob
import os
import shutil

count=0
image_directory_name= 'F:/Kirti_Swagat/2020_Business/stage_train/img'
mask_directory_name= 'F:/Kirti_Swagat/2020_Business/stage_train/mask'

image_array=[]
mask_array=[]

for img in glob.iglob("F:/Kirti_Swagat/2020_Business/stage_train/*/*/*"):
    base=os.path.basename(img)
    file= os.path.splitext(base)[1]
    #print(img)
    #print(base)
    #print(file)
    #if file=='.jpg':
        #shutil.copy(img, image_directory_name)
        #print(f"copying imgaes {file} to "+str(output_directory_name))
    #else:
        #shutil.copy(img, mask_directory_name)
        #print(f"copying imgaes {file} to "+str(mask_directory_name))
    image= cv2.imread(img)
    image= cv2.resize(image,(128,128,3))
    if file=='.jpg':
        image_array.append(image)
        print(file)
        print('Size of the Image array:',len(image_array))
    else:
        mask_array.append(mask)
        print(file)
        print('Size of the Mask array:',len(mask_array))
        
    
    
    #cv2.imwrite('F:/Kirti_Swagat/2020_Business/stage_train/copied_'+str(count)+'.jpg',image)