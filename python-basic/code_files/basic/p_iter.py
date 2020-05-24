#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 迭代器与生成器
list=[1,2,3,4]
it = iter(list)    # 创建迭代器对象

for x in list:
    print(x, end=" ")

for x in it:
    print(x, end=" ")
    print(x.__index__())
