#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 12/3/2018 4:22 PM
# @Author  : ZackChao
# @Site    : 
# @File    : list排序和过滤.py
# @Software: PyCharm


# 7、L=[1,2,3,1,2,3,2,4]要求：1.排序从大到小 2.过滤相同的数，相同的个数越多，排在前面 3.个数相同，元素从小到大排列 ？
# 分析：排序
#      过滤、统计
#
L=[1,2,3,1,2,3,2,4]
a=dict.fromkeys(L,0)    # dict记录元素个数

# 统计相同数
for i in L:  # 遍历L列表统计相同元素个数
    if i in a:
        a[i]+=1   # 判断key 获取相同元素个数

L=[(k,v) for k,v in a.iteritems()]

# 冒泡排序
for i in range(len(L)):
    for j in range(len(L)-1):
        if L[j][1]<L[j+1][1]:
            L[j],L[j+1]=L[j+1],L[j]
        elif L[j][0]<L[j+1][0]:
            L[j],L[j+1]=L[j+1],L[j]

print(L)
print([i[0] for i in L])  # list形式输出



# 8、去除列表中的重复元素，L=['b', 'c', 'd', 'c', 'b', 'a', 'a']
# 分析： set() 去重、 生成新列表not in、字典生成
#       sort()排序

L=['a','b','c','a','d','a']
L2=set(L)
L2.sort()
print(L2)

L2=dict.fromkeys(L).keys()



# *9、合并有序列表（尾递归），L1=[1,3,5,7,9]，L2=[2,4,6,8]
# 分析： 有序表  首数比较小的加入tmp 原表删除 一次重复 直到原表空。

def Combine(L1, L2, tmp):
    # 如果有一个列表为空，则直接将表添加进tmp尾部
    if not L1 or not L2:
        tmp.extend(L1)
        tmp.extend(L2)
        return tmp
    else:
        # 对两张表的第一个数进行比较，小的就添加进tmp，并删除列表中该数，依次重复，直至有一张表为空
        if L1[0] < L2[0]:
            tmp.append(L1[0])
            del L1[0]
        else:
            tmp.append(L2[0])
            del L2[0]
        return Combine(L1, L2, tmp)
