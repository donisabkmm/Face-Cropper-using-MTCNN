import os
import shutil

image = 'images/'
output = 'output/'
detached = 'failed/'

ip_list = os.listdir(image)
op_list = os.listdir(output)


for i in ip_list:
    if i not in op_list:
        shutil.copy(image+"\\"+i, detached)

