# /usr/bin/env python
# -*- coding:utf-8 -*-
import os, sys


'''
常用的操作文件路径的方法
'''


def listfiles(dirPath):
    files = []
    # root:dirpath
    # dirs:dirPath下所有子目录
    # files：dirPath下所有子文件
    for root, dirs, lists in os.walk(dirPath):
        for file in lists:
            files.append(file)
    print(files)
    return files



# 获取当前文件路径
def cur_file_dir():
    cur_dir = sys.path[0]
    if os.path.isdir(cur_dir):
        return cur_dir
    else:
        return os.path.dirname(cur_dir)


if __name__ == "__main__":
    print(cur_file_dir() )
