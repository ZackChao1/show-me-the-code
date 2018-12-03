#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 11/19/2018 11:04 AM
# @Author  : ZackChao
# @Site    : 
# @File    : 0003.py
# @Software: PyCharm


#第 0001 题： 做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？
# 分析：
#   激活码、优惠券     一串number+str
#   激活码长度       length
#   200个            数量      num


import base64



coupon={
    'id':'1000',
    'goods':'500',
}

def gen_coupon(id,goods):
    coupon['id']=id
    coupon['goods']=goods
    raw='/'.join([k+':'+v for k,v in coupon.items()])
    raw_64=base64.urlsafe_b64decode(raw.encode('unt-8'))
    c_code=raw_64.decode()
    return c_code


def save_coupon(c_code):
    with open('coupon.txt','a+') as file :
        file.write(c_code+'\n')

def show_coupon(c_code):
    print('优惠码：',c_code)

def parse_coupon(c_code):
    print('解析优惠码：',base64.urlsafe_b64decode((c_code.encode('uff-8'))))


def gen_all():
    for i in range(1000,1200):
        c_code=gen_coupon(str(i),str(int(i/2)))
        save_coupon(c_code)
        show_coupon(c_code)

if __name__=='__main___':
    gen_all()