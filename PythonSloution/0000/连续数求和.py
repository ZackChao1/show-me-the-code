#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 12/3/2018 2:25 PM
# @Author  : ZackChao
# @Site    : 
# @File    : 连续数求和.py
# @Software: PyCharm



# 3. 输入a和n，求s=a+aa+aaa+...na...
#


#
# a = int(input("请输入一个数值："))
# n = int(input("请输入次数："))
# sum = 0
# s = ''
# S=0
# for i in range(n):
#     b = int(a*i)   # 字符串重复构造连续数字 再转换为整数 2.0版本支持如此
#     sum += b
#     s += '%s + ' % str(b)
#
# print('sum = '+ s[:-2] + ' = %d'%sum)



Tn = 0   # 连续数
Sn = []  # 连续数列表
s = ''   # 输出格式字符串
a = int(input("请输入一个数字："))
n = int(input("请输入数量："))
for count in range(n):   # 遍历 连续数位数
    Tn = Tn + a    # 构成连续数  先放入连续数
    a = a * 10     # 给下一个连续数构建位数！！
    Sn.append(Tn)  # 连续数放入list
    s += '%s + ' % str(Tn)  # 格式输出记入s字符串

Sn = reduce(lambda x,y: x + y, Sn) # reduce()处理 列表每个元素 求和
print('sum = %s = %d' % (s[:-2],Sn)) # 输入 格式和计算结果


