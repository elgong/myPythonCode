from my_augmentation import *
import os
import numpy as np
from tqdm import tqdm

train_csv = open('train.csv')
aug_train_csv = open('aug_train.csv','a')
print('skip:' + train_csv.readline())
img_paths = []
for line in tqdm(train_csv):
    [img_name, data] = line.strip().split(',')
    img_paths.append('/home/deeplearning_xsfd/DBZ/my_train/'+img_name+'.jpg') 

for img in tqdm(img_paths):
    old_img = read_image(img)
    img_name = img.split('/')[-1][:-4]
    # save old img
    save_image(old_img,'/cu01_share/deeplearning_xfd/GEL/my_train_aug/'+img_name+'.jpg')    


    #horizontal_flip
    hor_img = horizontal_flip(old_img,rate=1)
    save_image(hor_img,'/cu01_share/deeplearning_xfd/GEL/my_train_aug/'+img_name+'_2'+'.jpg')

    #vertical_flip
    ver_img = vertical_flip(old_img, rate=1)
    save_image(ver_img,'/cu01_share/deeplearning_xfd/GEL/my_train_aug/'+img_name+'_3'+'.jpg')

    # rotation
    rot_img = random_rotation(old_img)
    save_image(ver_img,'/cu01_share/deeplearning_xfd/GEL/my_train_aug/'+img_name+'_4'+'.jpg')


