#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 11/20/2018 1:59 PM
# @Author  : ZackChao
# @Site    : 
# @File    : 0007.py
# @Software: PyCharm


# 有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来
# 分析：
#   dir path lines  count
#   null /n

import os,re


class countLines:
    def __init__(self):
        self.comment=0
        self.codes=0
        self.blank=0
        self.fileList=[]

    def openDir(self,dirname):
        curdir=os.getcwd()+str(dirname)
        dirlist=os.listdir(curdir)
        checkpy=re.compile(r"\.py$")
        for item in dirlist:
            if checkpy.search(item):
                item="\\"+item
                self.count(curdir+item)

    def count(self,filename):
        f=open(filename,'r',encoding='utf-8').read()
        patcomment=re.compile(r"^\s*#")
        patblank=re.compile(r"\s+$")
        for line in f:
            if patblank.search(line):
                self.blank+=1
            elif patcomment.search(line):
                self.comment+=1
            else:
                self.codes+=1
        self.fileList.append([filename,self.codes,self.comment,self.blank])

    def getResult(self):
        return self.fileList


if __name__=="__main__":
    countInstance=countLines();
    countInstance.openDir(r"\testDir")
    relist=countInstance.getResult()
    for item in relist:
        print(item[0])
        print("code num:"+str(item[1]))
        print("comment num :"+str(item[2]))
        print('blank num:'+str(item[3]))
        print("\n")
