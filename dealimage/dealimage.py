'''
Author: your name
Date: 2021-08-30 21:18:06
LastEditTime: 2021-08-31 22:46:53
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \pythontool\dealimage\dealimage.py
'''
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import cv2
import logging
from  threading import Thread


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

def get_new_size(infile):
    """
    按照手机浏览的规格（宽500）进行裁剪
    :param infile:
    :return:
    """
    img = cv2.imread(infile)
    height = img.shape[0]
    width = img.shape[1]
    phone_px = 500
    scale = float(phone_px) / width
    if width <= phone_px:
        return width,height
    else:
        height = int(height * scale)
    return phone_px, height

def convert_img_type(infile,):
    """
    将图片压缩到原来文件夹的webp下
    :param infile:
    :return:
    """
    encoder_path = "C:/Users/peng/Downloads/libwebp-1.0.0-windows-x64/bin/cwebp.exe"

    dir = '/'.join(infile.split('/')[0:-1])
    imgname = infile.split('/')[-1].split('.')[0]
    output_path = dir+"/webp/"

    if not os.path.exists(output_path):
        os.mkdir(output_path)

    new_size = get_new_size(infile)

    command = encoder_path + " -q 80 -resize " + str(new_size[0]) + " " + str(new_size[1]) + " " +infile + " -o "+output_path + imgname + ".webp"
    logging.debug(command)
    os.system(command)

def dirs(path):
    """
    多文件夹的递归遍历
    :param path:
    :return:
    """
    parents = os.listdir(path)
    for parent in parents:
        child = os.path.join(path, parent)
        if os.path.isdir(child):
            dirs(child)
        else:
            filepath = path + '/' + parent
            logging.info(filepath)
            # convert_img_type(filepath)
            t = Thread(target=convert_img_type, args=(filepath,))
            # t = Thread(target=convert_img_type_newwebpdir, args=(filepath,))
            t.start()
            t.join()




if __name__ == '__main__':
    path = "C:/Users/peng/Desktop/split"
    # cutImage(path)
    # rename_img(path)
    dirs(path)
