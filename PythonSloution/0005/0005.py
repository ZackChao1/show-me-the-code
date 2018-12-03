#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 11/20/2018 11:04 AM
# @Author  : ZackChao
# @Site    : 
# @File    : 0005.py
# @Software: PyCharm

'第 0005 题：你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率(1136x640)的大小。'
# 分析:
# 图片file    尺寸  1136*640
# image


from PIL import Image
import os,glob




def thumbnail_pic(path):
    a=glob.glob(r'*.png')   # 获取所有文件
    for x in a:
        name=os.path.join(path,x)   # 文件路径
        im=Image.open(name)
        im.thumbnail((1136,640))    # thumbnail() 调分辨率
        print(im.format,im.size,im.mode)
        im.save(name,'png')
    print('Done!')


if __name__=='__main__':
    path='.'
    thumbnail_pic(path)
