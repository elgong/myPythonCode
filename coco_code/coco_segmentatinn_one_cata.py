# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 13:25:20 2018

@author: GEL
"""
from PIL import Image
import cv2
import json
#from tqdm import tqdm
import numpy as np
from skimage import measure
from pylab import imshow
from pylab import array
from pylab import plot
from pylab import title
import matplotlib.pyplot as plt
import cv2



json_file = open('/home/elgong/Desktop/annotations/instances_train2017.json')
img_path = '/home/elgong/Desktop/mask/'
f = json.load(json_file)
#print('总共数量：',f["annotations"].length)
i = 0
now_img_id = '-'
segg = []
seggg = []
for data in f["annotations"]:
    img_id = data['image_id']
    category_id = data["category_id"]
    if now_img_id != img_id:
        print('New pic')
        now_img_id = img_id       
        img_name = '0'*(12 - len(str(now_img_id)))+str(now_img_id)+'.jpg'
        
    if category_id == 1:
        print(img_name)
        i+=1
        box = data['bbox']
        #seg = data['segmentation']
        img = cv2.imread(img_path+str(i)+img_name)

        img = img[int(box[1]):int(box[1]+box[3]),int(box[0]):int(box[0]+box[2])]
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = np.where(img > 50, 255,0)
        cv2.imwrite('/home/elgong/Desktop/mask2/'+str(img_name),img)
    del(img_id)
    del(category_id)
print('总共：', i)  
