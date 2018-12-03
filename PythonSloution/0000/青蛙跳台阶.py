#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 12/3/2018 3:49 PM
# @Author  : ZackChao
# @Site    : 
# @File    : 青蛙跳台阶.py
# @Software: PyCharm




# 5、一只青蛙一次可以跳上1级台阶，也可以跳上2级，求该青蛙跳上一个n级台阶总共有多少种跳法？
# 分析：  跳1级台阶   跳法f(1)=1
#        跳2级台阶   跳法f(2)=2
#            ... 类比
#        跳n级台阶   跳法,先跳1级剩下f(n-1)，再加先跳2级剩下f（n-2)；即f(n)=f(n-1)+f(n-2) ,也就是斐波那契数列！

fib=lambda n:n if n<=2 else fib(n-1)+fib(n-2)
# fib=lambda n,a=0,b=1:n if n==0 else fib(n-1,a,a+b)  尾递归:当递归调用是整个函数体中最后执行的语句且它的返回值不属于表达式的一部分时
print(fib(10))

def fib1(n):
    a=0
    b=1
    for i in range(n):
        a,b=b,a+b
    return b
print(fib1(10))


# 6、一只青蛙一次可以跳上1,2,3...n阶台阶，求该青蛙跳上一个n级的台阶有多少种方法？
# 分析： f(n)=f(n-1)+f(n-2)类比可知 f(n)=f(n-1)+f(n-2)+....f(n-n)=2f(n-1)
fib=lambda n:n if n<=2 else 2*fib(n-1)