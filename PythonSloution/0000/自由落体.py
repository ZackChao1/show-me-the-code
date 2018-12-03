#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 12/3/2018 3:39 PM
# @Author  : ZackChao
# @Site    : 
# @File    : 自由落体.py
# @Software: PyCharm



# 4、一球从100米高度自由落下，每次落地后反跳回原高度的一半，再落下，求他在第10次落地时，共经过多少米？第10次反弹多高？
# 分析， 高度100米   h
#        h=0.5*h   再落下  2h
#        10次   共经米数  sum1=2h , sum2=2h,...


h=100
hsum=0
for i in range(1,11):
    h=0.5*h
    hsum+=h*2

print(h,hsum)
