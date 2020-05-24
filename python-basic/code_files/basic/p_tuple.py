#!/usr/bin/env python
# -*- coding:utf-8 -*-

#1.元组
tuple1 = (1,2,3,4,5,6,7,8,9)
print(tuple1[0])

#2.元组中只要一个元素的时候需要加 , 都好，否则元组类型就变成了 int,如下
tuple2 = (1)
print(type(tuple2)) #<class 'int'>

tuple2 = (1,)
print(type(tuple2)) #<class 'tuple'>

#3.元组与列表的区别核心是逗号的区别

#4.重复操作符 * 乘号
tuple2 = 8*(1,)
print(tuple2)   #(1, 1, 1, 1, 1, 1, 1, 1)
tuple2 = 8*(1,2)
print(tuple2)   #(1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2)

#5.元组相关的操作符
#拼接操作符、
