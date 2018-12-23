import scipy.io
import numpy as np
import cv2
import os

inst_path = "/home/elgong/pictures/VOCdevkitSDS/new_inst/"
cls_path = "/home/elgong/pictures/VOCdevkitSDS/new_cls/"
img_path = "/home/elgong/pictures/VOCdevkitSDS/img/"

for _,__,files in os.walk(inst_path):
  for filename in files:  
    data = scipy.io.loadmat(inst_path+filename)
    data1 = scipy.io.loadmat(cls_path+filename)
    print np.max(data['GTinst']['Segmentation'][0][0])
    #print np.min(data['GTinst']['Segmentation'][0][0])
    img = data['GTinst']['Segmentation'][0][0]*100
    cv2.imshow('inst',img)
    img1 = data1['GTcls']['Segmentation'][0][0]*100
    cv2.imshow('cls',img1)
    img2 = cv2.imread(img_path+filename[:-4]+'.jpg')
    cv2.imshow('img',img2)
    cv2.waitKey(0)
'''
data = scipy.io.loadmat(inst_path)
#print data.keys()
#print data['GTinst']
#print data3['GTinst']['Segmentation'][0][0][250][150]
#print data3['GTinst']['Segmentation'][0][0][198][300]
#print data3['GTinst']['Segmentation'][0][0][250][470]
'''
