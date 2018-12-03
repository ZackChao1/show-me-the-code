#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 11/19/2018 10:45 AM
# @Author  : ZackChao
# @Site    : 
# @File    : 0000.py
# @Software: PyCharm'


#第 0001 题： 做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？
# 分析：
#   激活码、优惠券     一串number+str
#   激活码长度       length
#   200个            数量      num


import random

def make_number(num,length):
    str='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    # chars=string.letters+string.digits
    b=set()

    i=0
    while i<num:        # num激活码数量
        ans=''          # 激活码串结果
        for j in range(length):     #   根据激活码长度迭代
            ans+=random.choice(str)     # 随机挑选字符
        if ans not in b:    # 去重复
            b|={ans}        #
            i+=1
            print(ans)

if __name__=='__main__':
    make_number(200,18)