#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import markdown
import logging
from sql import Sql

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',datefmt='%a, %d %b %Y %H:%M:%S',)




# 所支持的复杂元素
exts = ['markdown.extensions.extra', 'markdown.extensions.codehilite','markdown.extensions.tables','markdown.extensions.toc']

# file_dir = input("输入需转换文件所在目录：")



def dirs(path):
    """
    多文件夹的递归遍历
    :param path:
    :return:
    """
    parents = os.listdir(path)
    ignore_path = ['.git','.gitattributes','R&D.md','README.md','SUMMARY.md']
    for parent in parents:    
        if (parent in ignore_path):
            logging.debug("忽略文件： " + parent)
            continue
        child = os.path.join(path, parent)
        if os.path.isdir(child):
            logging.debug("文件夹名称： " + child)
            dirs(child)
        else:
            filepath = path + '/' + parent
            logging.debug("文件名称及路径： " + filepath)
            md2html2db(filepath)



def md2html2db(filename):
    """
    转换md2html 插入数据库
    :return:
    """
    if filename[-3:] == '.md':
        html_body_file = open(filename,"r",encoding='utf-8')
        html_body_txt = html_body_file.read()
        html_body_file.close()

        md = markdown.Markdown(extensions = exts)
        html_body = md.convert(html_body_txt)
        # logging.debug(html_body)
        logging.debug("{}转换完毕".format(filename[:-3]))
        Sql.insert_posts(html_body,filename.split('/')[-1].split('.')[0])
    else:
        logging.error("非md文件，请检查 " + filename)

def md2html(filename):
    """
    转换md2html
    :return:
    """
    
    html_head = "<html>\n<body>\n"
    html_tail = "\n</body>\n</html>"
    html_body = ""

 
    if filename[-3:] == '.md':
        html_body_file = open(filename,"r",encoding='utf-8')
        html_body_txt = html_body_file.read()
        html_body_file.close()

        md = markdown.Markdown(extensions = exts)
        html_body = md.convert(html_body_txt)

        html = html_head + html_body + html_tail
        html_file = open(filename[:-3]+".html","w",encoding='utf-8')
        html_file.write(html)
        html_file.close()
        logging.debug("{}转换完毕".format(filename[:-3]))
    else:
        logging.error("非md文件，请检查")


def spiltPath():  
    src='C:/Users/peng/git/RenZhengfei/2018/20181121_任正非在日本研究所业务汇报.md'
    name = src.split('/')[-1].split('.')[0]
    print(name)

if __name__ == '__main__':
    path = 'C:/Users/peng/git/RenZhengfei/'
    dirs(path)
