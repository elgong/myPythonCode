# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 13:25:20 2018

@author: GEL
"""

import cv2 
import os
import numpy as np
import math

img_path = '/home/elgong/Desktop/my_code/img/'
mask_path = '/home/elgong/Desktop/my_code/mask/'
ro_img = '/home/elgong/Desktop/my_code/rotate_img/'
ro_mask = '/home/elgong/Desktop/my_code/rotate_mask/'

def rotate_about_center(src, angle, scale=1.):
    w = src.shape[1]
    h = src.shape[0]
    rangle = np.deg2rad(angle)  # angle in radians
    # now calculate new image width and height
    nw = (abs(np.sin(rangle)*h) + abs(np.cos(rangle)*w))*scale
    nh = (abs(np.cos(rangle)*h) + abs(np.sin(rangle)*w))*scale
    # ask OpenCV for the rotation matrix
    rot_mat = cv2.getRotationMatrix2D((nw*0.5, nh*0.5), angle, scale)
    # calculate the move from the old center to the new center combined
    # with the rotation
    rot_move = np.dot(rot_mat, np.array([(nw-w)*0.5, (nh-h)*0.5,0]))
    # the move only affects the translation, so update the translation
    # part of the transform
    rot_mat[0,2] += rot_move[0]
    rot_mat[1,2] += rot_move[1]
    return cv2.warpAffine(src, rot_mat, (int(math.ceil(nw)), int(math.ceil(nh))), flags=cv2.INTER_LANCZOS4)



 

files = os.listdir(img_path)
count = 0
for img_name in files:
    img = cv2.imread(img_path + img_name)
    mask = cv2.imread(mask_path + img_name)
    rand_angle = np.random.randint(-30, 30)  # 随机角度
    shape = img.shape
    if shape[0] > 100 and shape[1] > 100:
        count += 1
        rotate_img = rotate_about_center(img, angle = rand_angle, scale=1.)
        rotate_mask  = rotate_about_center(mask, angle = rand_angle, scale=1.)


        box = np.where(rotate_mask > 254)
        x_min = min(box[0])
        x_max = max(box[0])

        y_min = min(box[1])
        y_max = max(box[1])

        rotate_img = rotate_img[ x_min: x_max, y_min:y_max ]
        rotate_mask = rotate_mask[ x_min: x_max, y_min:y_max ]
        cv2.imwrite(ro_img + str(img_name), rotate_img)
        cv2.imwrite(ro_mask +str(img_name) ,rotate_mask)
print(count)
