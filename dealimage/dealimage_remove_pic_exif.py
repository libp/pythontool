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
import piexif

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',datefmt='%a, %d %b %Y %H:%M:%S',)

def get_new_size(infile):
    """
    按照手机浏览的规格（宽500）进行裁剪
    :param infile:
    :return:
    """
    img = cv2.imread(infile)
    height = img.shape[0]
    width = img.shape[1]
    print(width,height)

    # remove pic exif 
    # 图片纵横比失真。这个方式不行！
    piexif.remove(infile)

    phone_px = 2000
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
    # encoder_path = "C:/Users/peng/Downloads/libwebp-1.0.0-windows-x64/bin/cwebp.exe"
    encoder_path = "C:/Users/peng/Downloads/libwebp-1.3.0-windows-x64/bin/cwebp.exe"

    dir = '/'.join(infile.split('/')[0:-1])
    imgname = infile.split('/')[-1].split('.')[0]
    output_path = dir+"/webp/"

    if not os.path.exists(output_path):
        os.mkdir(output_path)

    new_size = get_new_size(infile)
    print(new_size[0],new_size[1])

    command = encoder_path + " -quiet -q 85 -resize " + str(new_size[0]) + " " + str(new_size[1]) + " " +infile + " -o "+output_path + imgname + ".webp"

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
            t.start()
            t.join()




if __name__ == '__main__':
    # path = "C:/Users/peng/Desktop/test/111"
    # path = "C:/Users/peng/Desktop/test/1518638008875028482"
    path = "C:/Users/peng/Desktop/test/1518627669293506561"

    dirs(path)
