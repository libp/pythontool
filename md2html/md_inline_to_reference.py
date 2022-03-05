#coding:utf-8

import sys
import re
import logging
import os

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',datefmt='%a, %d %b %Y %H:%M:%S',)


def dirs(path):
    """
    多文件夹的递归遍历
    :param path:
    :return:
    """
    parents = os.listdir(path)
    print(parents)
    ignore_path = ['.git','.gitattributes','R&D.md','README.md','SUMMARY.md','目录.md']
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
            md_inline_to_reference(filepath)




def md_inline_to_reference(filepath):
    """
    转换md_inline_to_reference
    :return:
    """
    if filepath[-3:] == '.md':
        md_inline = open(filepath,"r",encoding='utf-8')
        content = md_inline.read()
        md_inline.close()
        content = content.replace('（完）','## References'+'\n\n')

        # 匹配图片，语法格式为 ![]()
        matches = re.compile('[^!](\\[.*?\\]\(.*?\))').findall(content)
        print('total url : {0}'.format(matches))

        index = 0
        for match in matches:
            index = index + 1
            #re method
            title = re.compile('\\[(.*?)\\]').search(match).group(1)
            url = re.compile('\((.*?)\)').search(match).group(1)
            #splite method
            # title = match.split(']')[0].split('[')[1]
            # url = match.split('(')[1].split(')')[0]
            logging.debug(str(index) + ' ' + title + ' ' + url)

            footnote_mark = title + '<sup>'+str(index)+'</sup>'
            content = content.replace(match, footnote_mark)

            footnote_line = '<code>' + '[' + str(index) + '] ' + '</code>' + title+ ': ' + '<em>' + url + '</em>' +'\n<br>'
            content = content + footnote_line

        newfilepath = filepath.replace('docs','temp')
        open(newfilepath,"w",encoding='utf-8').write(content)

    else:
        logging.error("非md文件，请检查")

if __name__ == '__main__':
    path = 'C:/Users/peng/git/weekly/docs/'
    dirs(path)
    # path = 'C:/Users/peng/git/weekly/docs/issue-1.md'
    # md_inline_to_reference(path)