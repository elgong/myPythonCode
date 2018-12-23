import os


path = '/home/elgong/Desktop/my_code/rotate_img/'
right_img_name = open('/home/elgong/Desktop/my_code/img_name.txt')

right_img_list = []
for line in right_img_name:
    right_img_list.append(line.strip())

#print(right_img_list[:100])

print(len(right_img_list))
files = os.listdir(path)
j = 0
for i in files:
    if i not in right_img_list:
        os.remove(path+str(i))
