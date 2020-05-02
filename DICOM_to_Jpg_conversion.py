import pydicom as dicom
import os
import cv2
import PIL # optional
import time

start_time= time.time()
# make it True if you want in PNG format
PNG = False

# Specify the .dcm folder path
folder_path = 'F:/Kirti_Swagat/AI/COVID_19_Predictions/Data_Sets/22_04_2020_for_COVID_NET_model/kaggel_data_set/stage_2_test_images'

# Specify the output jpg/png folder path
jpg_folder_path = 'F:/Kirti_Swagat/AI/COVID_19_Predictions/Data_Sets/22_04_2020_for_COVID_NET_model/kaggel_data_set/stage_2_test_jpg'

images_path = os.listdir(folder_path)

#print(images_path)

#for n, image in enumerate(images_path):
    #print(image)


for n, image in enumerate(images_path):
    ds = dicom.dcmread(os.path.join(folder_path, image))
    pixel_array_numpy = ds.pixel_array
    if PNG == False:
        image = image.replace('.dcm', '.jpg')
    else:
        image = image.replace('.dcm', '.png')
    cv2.imwrite(os.path.join(jpg_folder_path, image), pixel_array_numpy)
    if n % 50 == 0:
        print('{} image converted'.format(n))

end_time= time.time()
print('Total time in seconds:',format(end_time-start_time,'.2f'))
