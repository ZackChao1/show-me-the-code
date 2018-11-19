#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 10/30/2018 10:26 AM
# @Author  : Aries
# @Site    : 
# @File    : 0001.py
# @Software: PyCharm




# 第 0000 题： 将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。

from PIL import Image,ImageFont,ImageDraw


def write_number(image_file_path,number=1):     # 写入数字函数，参数：图片路径和数字
    img=Image.open(image_file_path)     # image.open()打开图片
    number_txt = str(number) + '' if number < 100 else '99+'  # 取num

    # handle font
    font_size=int((img.size[0] if img.size[0]<img.size[1] else img.size[1])/4)   # 字体大小 取图片长度X/4
    font=ImageFont.truetype("arial.ttf",size=font_size)     # 设定字体类型
    if font.getsize(number_txt)[0] >img.size[0] or font.getsize(number_txt)[1] > img.size[1]:   # 字体比图片大直接返回图片
        return img

    # handle position
    position=img.size[0]-font.getsize(number_txt)[0]    # 计算X位置 图片X - 字体X
    ImageDraw.Draw(img).text((position,0),number_txt,(255,0,0),font)        # draw num
    return img      # 返回 image对象

write_number('zzc.jpg').save('result.png')  # image对象保存
write_number('zzc.jpg',100).save('result100.png')
num=78
write_number('zzc.jpg',num).save('result%d.png' % num )



