'''
Author: your name
Date: 2021-08-30 21:18:06
LastEditTime: 2021-08-31 22:19:33
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \pythontool\dealimage\dealimage.py
'''
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import cv2
import logging


logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',datefmt='%a, %d %b %Y %H:%M:%S',)

def cutImage(path):
    listdir = os.listdir(path)
    
    newdir = os.path.join(path, 'split')    # make a new dir in dirpath.
    if(os.path.exists(newdir) == False):
        os.mkdir(newdir)
        
    for i in listdir:
        if i.split('.')[1] == "jpg":	
            filepath = os.path.join(path, i)
            filename = i.split('.')[0]
            leftpath = os.path.join(newdir, filename) + "_left.jpg"
            rightpath = os.path.join(newdir, filename) + "_right.jpg"

            img = cv2.imread(filepath)
            [h, w] = img.shape[:2]
            logging.debug("文件路径和高宽： " + filepath, (h, w))

            limg = img[:, :int(w/2), :]
            rimg = img[:, int(w/2+1):, :]

            cv2.imwrite(leftpath, limg)
            cv2.imwrite(rightpath, rimg)




def rename_img(path):
    """
    对图片排序后改名
    :param path:
    :return:
    """
    imgs = os.listdir(path)
    for i,fi in enumerate(imgs):
        old_name=os.path.join(path,fi)
        new_name=os.path.join(path,str(i+2)+'.jpg')
        print(new_name)
        os.rename(old_name,new_name)




if __name__ == '__main__':
    path = "C:/Users/peng/Desktop/split"
    # cutImage(path)
    rename_img(path)