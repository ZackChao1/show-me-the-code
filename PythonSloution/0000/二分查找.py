#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 12/3/2018 4:23 PM
# @Author  : ZackChao
# @Site    : 
# @File    : 二分查找.py
# @Software: PyCharm




# 10、通过不断对半的方法查找区间[a,b]内的数值位置？
# 分析：  L=[a,b]里找t位置

def binarySearch(list,item):
    low,hight=0,len(L)-1   # 跟踪区间头和尾
    while low<=hight:
        mid=(low+hight)/2  # 中间位置
        guess=list[mid]
        if  guess>item:   # 大于中间的数
            hight=mid -1  # 调整区间尾部为中间位置
        elif guess<item:  # 小于中间的数
            low=mid+1   # 调整头位置右移
        else:
            return mid   # 直到L[mid]==t 返回当前位置mid
        return None





