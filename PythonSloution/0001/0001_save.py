#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 11/19/2018 11:34 AM
# @Author  : Aries
# @Site    : 
# @File    : 0001_save.py
# @Software: PyCharm


#  将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。
# 分析：
#   保存   def save(dic)
#   mysql库  connect()----cursor()----execute()----commit()----close()
#   sqlLite库    connect('test.db))----cursor()----execute()---rowcount() fetchall(0---close()

import random

def make_number( num, length ):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    dic = set()
    i = 0
    while i < num:
        str = ''
        for j in range(length):
            str += random.choice(letters)
        if str not in dic:
            dic |= {str}            #
            i += 1
        else:
            continue
    return dic

def save(dic,db='mysql'):
    if db:
        import pymysql
        # mysql database
        conn=pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            passwd='pass@word01'        # connect()连接mysql
        )
        cur=pymysql.cursors()           # cursors() 实例游标对象

        try:
            __create='create database if not exists test'   # 建test database
            cur.execute(__create)           # 执行建test database
        except:                             # 建test database 异常 输出error
            print('database create error')

        conn.select_db('test')      # select_db() use test database
        __create_table='create table if not exists code(code char(64))'
        cur.execute(__create_table)         # create table
        cur.executemany('insert into code values(%s)' ,dic)    # insert data dic

        conn.commit() # 提交事务
        cur.close()     # 关闭游标对象
        conn.close()    # 关闭连接
    else:
        import sqlite3
        conn=sqlite3.connect('test.db')
        cur=conn.cursor()
        # __create = "create database if not exists test"
        # cur.execute(__create)
        __create_table = "create table if not exists code(code char(64))"
        cur.execute(__create_table)
        print(dic)
        cur.executemany('insert into code values (?)',dic)
        cur.close()
        conn.commit()
        conn.close()


if __name__=='__main__':
    save(make_number(100,11),'')



