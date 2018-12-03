#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 11/19/2018 3:44 PM
# @Author  : ZackChao
# @Site    : 
# @File    : 0004.py
# @Software: PyCharm


# 第 0004 题： 任一个英文的纯文本文件，统计其中的单词出现的个数。
# 分析：
#      文本文件     with open as    read()  --->data
#       个数      num
#       单词      words
#       英文      a-zA-Z  re.compile()
#       统计出现   输出单词，个数      dict(key,value)


import re

with open ('input.txt','r') as f:
    data=f.read()

words=re.compile(r'([a-zA-Z]+)')
dic={}  # 字典key用来记录单词，value用来记录次数 {'单词'：次数}
for x in words.findall(data):   # 从data里匹配words 并计数
    if x not in dic:
        dic[x]=1        # 不在dic，计数给1
    else:
        dic[x]+=1       # 在dic里，计数累加

L=[]
for k,value in dic.items():
    L.append((k,value))     # 以tuple形式追加到列表
L.sort(key=lambda t:t[0])   # 按首字符顺序排序
for x in L:
    print(x[0],x[1])        # 输出字符，个数





