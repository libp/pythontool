#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import markdown

html_head_file = open("html_head.txt","r",encoding='utf-8')
html_head = html_head_file.read()
html_head_file.close()

html_tail = "\n</body>\n</html>"
html_body = ""

# 所支持的复杂元素
exts = ['markdown.extensions.extra', 'markdown.extensions.codehilite','markdown.extensions.tables','markdown.extensions.toc']

file_dir = input("输入需转换文件所在目录：")

for filename in os.listdir(file_dir):
    if filename[-3:] == '.md':
        html_body_file = open(file_dir+filename,"r",encoding='utf-8')
        html_body_txt = html_body_file.read()
        html_body_file.close()

        md = markdown.Markdown(extensions = exts)
        html_body = md.convert(html_body_txt)

        html = html_head + html_body + html_tail
        html_file = open(file_dir+filename[:-3]+".html","w",encoding='utf-8')
        html_file.write(html)
        html_file.close()
        print("{}转换完毕".format(filename[:-3]))
