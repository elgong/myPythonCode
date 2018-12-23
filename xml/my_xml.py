# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 10:34:27 2018

@author: Administrator
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 10:01:24 2018

@author: Administrator
"""

import xml.etree.ElementTree as ET
'''
方法：
findall(match)  # 返回所有匹配的子元素列表
iter(tag=None)   # 以当前元素为根节点 创建树迭代器,如果tag不为None,则以tag进行过滤

属性相关：

    attrib             为包含元素属性的字典
    keys()             返回元素属性名称列表
    items()             返回(name,value)列表
    get(key, default=None)  获取属性
    set(key, value)         跟新/添加  属性
    del xxx.attrib[key]    删除对应的属性
    
元素相关：

删除子元素  remove()

'''
### 解析成 tree
tree = ET.parse('/home/elgong/Desktop/a.xml')


### 获取 根节点
root = tree.getroot()



######################### 查找  #####################
### 方法 1
### 遍历xml 文档
# 打印第 2 层的 标签名字和属性
for layer2_child in root:
    print(layer2_child.tag,':',layer2_child.attrib)
    # 打印第 3 层的 标签名字和属性，文本
    for layer3_child in layer2_child:
        print(layer3_child.tag,':',layer3_child.attrib,layer3_child.text)
        

'''
### 方法 2
### 可以直接按照位置 寻找节点
year = root[0][1].text

### 方法 3
# 过滤出所有neighbor标签
for neighbor in root.iter("neighbor"):
    print(neighbor.tag, ":", neighbor.attrib)
    
###方法 4
# 遍历所有的counry标签
for country in root.findall("country"):
    # 查找country标签下的第一个rank标签
    rank = country.find("rank").text
    # 获取country标签的name属性
    name = country.get("name")
    print(name, rank)
    
###################  修改 ###############################

### 1. 修改text ,并且添加属性
for rank in root.iter('rank'):
    new_rank = int(rank.text)+1
    rank.text = str(new_rank)  ### to string
    rank.set('updated','yes')

### 2. 删除属性
for rank in root.iter('rank'):
    # 删除 updated属性
    del rank.attrib['updated']
    
    
###################### 新建和保存######################
import xml.etree.ElementTree as ET
from xml.dom import minidom


def subElement(root, tag, text):
    ele = ET.SubElement(root, tag)
    ele.text = text


def saveXML(root, filename, indent="\t", newl="\n", encoding="utf-8"):
    rawText = ET.tostring(root)
    dom = minidom.parseString(rawText)
    with open(filename, 'w') as f:
        dom.writexml(f, "", indent, newl, encoding)


root = ET.Element("note")

to = root.makeelement("to", {})
to.text = "peter"
root.append(to)

subElement(root, "from", "marry")
subElement(root, "heading", "Reminder")
subElement(root, "body", "Don't forget the meeting!")

# 保存xml文件
saveXML(root, "note.xml") 

'''
