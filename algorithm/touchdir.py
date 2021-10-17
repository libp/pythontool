#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import datetime

def round6():
    for i in range(0,10):
        for j in range(0,10):
            for k in range(0,10):
                for l in range(0,10):
                            mkdir(i,j,k,l)


def mkdir(i,j,k,l):  
    path = "C:/Users/peng/Documents/buildup/" + str(i) + "/" + str(j) + "/" + str(k) + "/" + str(l)
    os.makedirs( path )
    tmp_file = open(path+"/tmp.txt","w",encoding='utf-8')
    tmp_file.write("hello world")
    tmp_file.close()

if __name__ == '__main__':
    start = datetime.datetime.now()
    round6()
    end = datetime.datetime.now()
    print("Time used:",end - start)
