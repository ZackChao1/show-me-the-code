#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 11/19/2018 9:43 AM
# @Author  : Aries
# @Site    : 
# @File    : 0002.py
# @Software: PyCharm




# 第 0000 题： 将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。
# 分析：
#   QQ头像    一张图片 imageFile
#   红色数字    一个num   number red
#   右上角     num位置   num_position
#   ----> def add_num(image_name,number)

from PIL import Image,ImageFont,ImageDraw

def img_add_number(image_name,number):
    img=Image.open(r'zzc.jpg')


    w=img.width
    h=img.height
    print(h,w)

    fnt=ImageFont.truetype('arial.ttf',int(h/4))     # 字体大小15%
    position = img.size[0] - fnt.getsize(number)[0]  # 计算X位置 图片X - 字体X
    ImageDraw.Draw(img).text((position,0),number,fill=(255,0,0),font=fnt)    # 文本大小 ,应同字体大小相适应
    img.save(image_name.split('.')[0]+'2.jpg')


if __name__=='__main__':
    img_add_number('zzc.jpg','53')
