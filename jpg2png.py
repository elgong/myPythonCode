import numpy as np
import os
import cv2

 
mask_path = '/home/elgong/Desktop/my_code/rotate_mask/'
save_path = '/home/elgong/Desktop/my_code/test/'
img_list = os.listdir(mask_path)

for img_name in img_list:
    img = cv2.imread(mask_path+img_name,0)
    now_img = np.where(img < 50, 0, 1)
    cv2.imwrite(save_path+img_name[:-4]+'.png',now_img)
