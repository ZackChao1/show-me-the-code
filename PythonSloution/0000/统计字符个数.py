#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 12/3/2018 11:28 AM
# @Author  : ZackChao
# @Site    : 
# @File    : 统计字符个数.py
# @Software: PyCharm


# 2、输入一行字符， 分别统计出其中英文字母、空格、数字和其它字符的个数。
# 分析： 字符串  input()
#       a-zA-Z 0-9
#        BIF,isalpha() isspace() isdigit()

s=input('输入一个字符串：')
letters=space=digit=other=0
print(s,len(s))
for i in s:
    if i.isalpha():
        letters+=1
    elif i.isspace():
        space+=1
    elif i.isalnum():
        digit+=1
    else:
        other+=1

print('字母数量为%d,空格数量为%d,数字数量为%d,其他数量为%d' % (letters,space,digit,other))




