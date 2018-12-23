
import cv2
import os
import numpy as np
from tqdm import tqdm
'''
img_name = os.listdir('/home/elgong/Desktop/my_code/img')


img_dict = {}
for i in img_name:
    org_img = i[-16:]
    n_img = i[:-16]
    #print(org_img)
    if org_img not in img_dict:
        img_dict[org_img] = [n_img]
    else:
        img_dict[org_img].append(n_img)

print(len(img_dict))

for key in tqdm(img_dict.keys()):
    i = 1
    for n_img in img_dict[key]:
        if i == 1:
            now_mask = cv2.imread('/home/elgong/Desktop/my_code/mask/'+str(n_img)+str(key),0)
            now_mask = np.where(now_mask > 50,255, 0)/255*i
        else:
            mask = cv2.imread('/home/elgong/Desktop/my_code/mask/'+str(n_img)+str(key),0)
            mask = np.where(mask > 50,255,0)/255*i
            Unow_mask = now_mask.copy()
          #  print('----------------------')
           # print(Unow_mask)
            Unow_mask = np.where(Unow_mask !=0 ,0, 1)
           # print('----------------------')
           # print(Unow_mask)
            mask = Unow_mask * mask
            now_mask += mask
       # now_mask = np.where(now_mask==0, 0, 255)
       # sum_img = sum_img + now_img/255*i*50
        i+=1
    #print("person: " ,i-1,"   sum : ",np.max(now_mask))
    #if((i-1)*20 < np.max(now_mask)):
        #now_mask = np.where(now_mask == np.max(now_mask))
   

    img = cv2.imread('/home/elgong/Desktop/my_code/img/'+str(n_img)+str(key))
    #cv2.imshow('img',img)
   # cv2.imshow('mask',now_mask)
    cv2.imwrite('/home/elgong/Desktop/my_code/iimage/'+str(key[:-4])+'.jpg',img)
    cv2.imwrite('/home/elgong/Desktop/my_code/mmask/'+str(key[:-4])+'.png',now_mask)
    #img2 = cv2.imread('/home/elgong/Desktop/my_code/mmask/'+str(key[:-4])+'.png')
    #cv2.imshow('mask',img2)
    #cv2.waitKey(0)
'''
img = cv2.imread('/home/elgong/Desktop/my_code/mask/7000000143908.jpg',0)
cv2.imshow('img',img*20)

cv2.waitKey(0)



