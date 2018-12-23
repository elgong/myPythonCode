import cv2
import os
from tqdm import tqdm
import numpy as np
import scipy.io as scio
import random


imgPath = '/home/elgong/Desktop/my_code/rotate_img/'
maskPath = '/home/elgong/Desktop/my_code/rotate_mask/'
imgSavePath = '/home/elgong/Desktop/coco_mat/img/'
clsSavePath = '/home/elgong/Desktop/coco_mat/cls/'
instSavePath = '/home/elgong/Desktop/coco_mat/inst/'
maskSavePath = '/home/elgong/Desktop/coco_mat/mask/'	
for _,__,files in os.walk(imgPath):
    for name in tqdm(files):
        mask = cv2.imread(maskPath+name,0)
        img = cv2.imread(imgPath+name)

        newImg = cv2.resize(img,(224,224))
        newMask = cv2.resize(mask,(224,224))
        newMask = np.where(newMask==0,0,1)
        cv2.imwrite(imgSavePath+name,newImg)
        cv2.imwrite(maskSavePath+name,newMask)
        scio.savemat(clsSavePath+name[:-4]+'.mat',{'GTcls':newMask})
        scio.savemat(instSavePath+name[:-4]+'.mat',{'GTinst':newMask})
