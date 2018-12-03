#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 11/20/2018 11:25 AM
# @Author  : ZackChao
# @Site    : 
# @File    : 00006.py
# @Software: PyCharm

#你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词
# 分析：
#   dir path  filenameXX.txt [a-zA-Z]
#   words   count       获取单词出现次数



import glob,os,re
from collections import OrderedDict


def search_words(words,path='.'):
    files=glob.glob(r'*.txt')
    dic={}
    for y in files:
        name=os.path.join(path,y)   # path+filename
        data=open(name,'r').read()
        w = re.compile(r'([a-zA-Z]+)')
        for x in w.findall(data):
            if x not in dic:
                dic[x]=1
            else:
                dic[x]+=1       # 对应的key的value累加次数


    for z in words:
        print(dic[z])


def get_num(word,filename):
    with open(filename,'r') as f:
        words=re.compile(r'[\s\,\;\n]{1}'+word+r'[\s\,\;\.\n]{1}')
        numbers=words.findall(f)
        return len(numbers)

def article_analysis(dirs):
    article=glob.glob(r'*.txt')
    dictdata=OrderedDict()
    for m in article:
        doc=open(m,'r',encoding='utf-8').read()
        doc=re.findall(r'[\w\-\_\,]+',doc)
        doc=list(map(lambda x :x.strip('.'),doc))
        for n in doc:
            dictdata[m]=get_num(n,m)
        a=OrderedDict(sorted(dictdata.items(),key=lambda x:x[1],reverse=True))
        print('在%s中出现次数最多的单词是：' % m)
        for  c in a:
            print(c+':%s' % a[c])
            break
    return 0


if __name__=='__main__':
    words=['zzc','zj']
    search_words(words)