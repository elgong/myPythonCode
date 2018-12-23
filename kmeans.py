# -*- coding: utf-8 -*-

"""
@author ZibinPan
Created on Tue Feb 27 14:24:29 2018
sklearn k-means聚类实用封装库
用法：传入的参数均为list类型，x1为x坐标，x2为y坐标，types_num为聚类数，types为各类的名称,colors为各类点的颜色，shapes为各类点的形状
返回一个kmeans_model对象，其labels_属性记录着聚类的标签（如0，1，2等），cluster_centers_属性记录着聚类的中心
另外也返回聚类后的x1_result和x2_result对象，x1_result记录着原x1列表的聚类结果，
    即x1_result列表中有n个元素（n为聚类数），其中每个元素都是一个列表（原x1列表中属于该类的所有元素组成的列表）
x2_result同上
"""
 
import numpy as np  
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
 
def kmeans_building(x1,x2,types_num,types,colors,shapes):
    X = np.array(list(zip(x1, x2))).reshape(len(x1), 2)  
    kmeans_model = KMeans(n_clusters=types_num).fit(X) # 设置聚类数n_clusters的值为types_num
    # 整理分类好的原始数据, 并画出聚类图
    x1_result=[]; x2_result=[]
    for i in range(types_num):
        temp=[]; temp1=[]
        x1_result.append(temp)
        x2_result.append(temp1)
    for i, l in enumerate(kmeans_model.labels_):  # 画聚类点
        x1_result[l].append(x1[i])
        x2_result[l].append(x2[i])
        plt.scatter(x1[i], x2[i], c=colors[l],marker=shapes[l])
    for i in range(len(list(kmeans_model.cluster_centers_))): # 画聚类中心点
        plt.scatter(list(list(kmeans_model.cluster_centers_)[i])[0],list(list(kmeans_model.cluster_centers_)[i])[1],c=colors[i],marker=shapes[i],label=types[i],s = 1)
    plt.legend()
    plt.show()
    return kmeans_model,x1_result,x2_result


kmeans_building(x,y,2, ['zheng', 'fan'], ['r','g'],['o', 's', 'D'])
