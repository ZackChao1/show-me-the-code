#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 12/3/2018 10:37 AM
# @Author  : ZackChao
# @Site    : 
# @File    : 因式分解.py
# @Software: PyCharm



# 1、输入一个正整数n,对其因式分解并输出；
# 分析：（伪步骤）
# 正整数n input()  int()
# 从最小质数2遍历 n%i==0 i为质数 ，n=n/i 作为新正整数从2开始遍历，
# 循环直到n==i 因式分解结束
#
n=int(input("输入一个正整数："))
b=""   # 存分解结果
d=n    # 显示源正整数
q=1  # 标记因式分解是否继续
while q:
    if n == 1:    # 排除n=1的情况
        break
    for i in range(2,n+1):  # 从2遍历到正整数
        if n%i==0:
            b+='%s*'%i   # 结果放入b
            n=int(n/i)   # 重置n,最好结果为自己
            break
        if n==i:
            q=0
            break

print('%s=%s%s' %(d,b,n))


from sys import stdout
n=int(input("输入一个正整数："))
b=n   # 留源正整数
print('n=%s' %n) # 显示源内容
stdout.write(str(n)+" = ")  # 构建输出结果n=

for i in range(2,n+1):
    while n!=1:
        if n % i==0:
            stdout.write(str(i))   # 把当前分解到的因子输出不换行
            stdout.write("*")   # 输出 *
            n = n / i  # 重置n为分解的下一个数
            if n==1:   # 下一个被分解数为1情况
                n*=i
        else:
            break
print('%d' %n)




