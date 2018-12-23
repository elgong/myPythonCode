# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 13:25:20 2018

@author: GEL
"""

from PIL import Image
import cv2
import json
import numpy as np
from skimage import measure,data,color
from PIL import Image
from pylab import imshow
from pylab import array
from pylab import plot
from pylab import title
import numpy as np
import matplotlib.pyplot as plt
import io

###### 一些参数

category_id = 1    # 要切割的某个种类, 1对应人体
save_segmentation_path =  '/home/elgong/Desktop/my_code/mask/'   #要切割的物体， 画出边缘并且填涂颜色( 背景黑色， 物体白色)
save_img_path = '/home/elgong/Desktop/my_code/img/'  # 要切割的物体对应的原图，根据 bbox将该物体裁出来后保存

######



def draw_line(img_path, save_path,xy_list):
    '''
    画出物体的边缘，并且填涂颜色
    img_path:
    save_path	
    '''
    from PIL import Image
    from pylab import imshow,save
    from pylab import array
    from pylab import plot
    from pylab import title
    import numpy as np
    import matplotlib.pyplot as plt
    from skimage import measure,data,color
    import cv2

 # 读取图像到数组中
    im = array(Image.open(img_path))  

# 减去自己， 使图像变成黑色，作为背景色，之后根据xy_list的 segmentation 坐标添涂前景颜色
    im = im - im   
    imshow(im)

    fig = plt.gcf()
    fig.set_facecolor('black')

# coco 数据集中有部分图像是 “单通道”
    if len(im.shape)==3:   
        height, width, channels = im.shape
    elif len(im.shape) == 2:
        height, width = im.shape

# 如果dpi=300，那么图像大小=height*width
    fig.set_size_inches(width/100.0/3.0, height/100.0/3.0)
    plt.gca().xaxis.set_major_locator(plt.NullLocator())
    plt.gca().yaxis.set_major_locator(plt.NullLocator())
    plt.subplots_adjust(top=1,bottom=0,left=0,right=1,hspace=0,wspace=0)
    plt.margins(0,0)
    for i in range(len(xy_list)):
        hand = np.array(xy_list[i])
        new_hand = hand.copy()
        for _ in range(5):
            new_hand =measure.subdivide_polygon(new_hand, degree=2)
        appr_hand =measure.approximate_polygon(new_hand, tolerance=0.02)
	
	# 画出 segmentation 边界
        plt.plot(new_hand[:, 0], new_hand[:, 1],'r',linewidth=0.5,color = 'white')
        plt.xticks([])
        plt.yticks([])
        plt.axis('off') 
	# 填涂颜色
        plt.fill(new_hand[:, 0], new_hand[:, 1], facecolor='white',alpha=1)   
    plt.close()

    fig.savefig(save_path, format='jpg', transparent=True, dpi=300, pad_inches = 0)
    del(xy_list)














json_file = open('/home/elgong/dataset/coco/annotations/instances_train2017.json')
img_path = '/home/elgong/dataset/coco/train2017/'
f = json.load(json_file)

i = 0  # 记录处理的图像数量，并作为新名字的一部分
now_img_id = '-'  # 记录当前处理的图片名
segg = []
seggg = []

# f["annotations"] 是 instances_train2017.json 中每一个事物对应的信息
for data in f["annotations"]:
    #print(data)
    segg = []
    seggg = []
    category_id = 1
    img_id = data['image_id']         # 'image_id'       对应图片名
   # print(img_id)
    category = data["category_id"] # "category_id"    对应种类
    #print(img_id)
    if now_img_id != img_id: 
        now_img_id = img_id 
        img_name = '0'*(12 - len(str(now_img_id)))+str(now_img_id)+'.jpg'  # 转换成真实图片名
        #print(img_name)
    if category_id == category:   # 选择需要切割的种类
        i+=1
        box = data['bbox']

        seg = data['segmentation']
        img = cv2.imread(img_path+img_name)

        # 每个 data['segmentation'] 对应一个物体，但是每个物体不一定只有一块，当出现遮挡的情况，需要多块都切割出来
	# jj: 这个物体被分成的块数
	# 
        for jj in range(len(seg)): # len(seg) 对应一个人 分割出来的块数，
            for s in range(int(len(seg[jj])/2)):
                segg.append([seg[jj][s*2],seg[jj][s*2+1]])
            segg.append([seg[jj][0],seg[jj][1]])  # 保证曲线闭合
            seggg.append(segg)
            segg = []

	# 画出物体的边缘，并且填涂颜色，保存图片
        draw_line(img_path+img_name,  save_segmentation_path +str(i)+str(img_name),seggg)
        del(segg)
        del(seg)
        del(seggg)

	# 根据bbox 裁剪 原图像
        #img = img[int(box[1]):int(box[1]+box[3]),int(box[0]):int(box[0]+box[2])]
        cv2.imwrite('/home/elgong/Desktop/my_code/img/'+str(i)+str(img_name),img)
    del(img_id)
    del(category_id)
print('总共：', i)  
