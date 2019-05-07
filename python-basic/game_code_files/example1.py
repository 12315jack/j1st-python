#!/usr/bin/env python
# -*- coding:utf-8 -*-

import random

print('---------------------happy study python------------------')

guess=random.randint(1,10)
while guess!=8:
    temp = input("猜猜用户输入的数字是多少？：")
    guess = int(temp)
    if guess == 8:
        print("哈哈，你真牛逼，这都能猜得到")
        print("不过猜中了也没用，哈哈哈，洗洗睡吧")
    else:
        if (8 - guess) > 0:
            print("猜的数字小了")
            guess = int(input("请输入一个大一点的数"))
        else:
            print("猜的数字太大了")
print("游戏结束，好无聊，拜拜")


# builtins dir(__builtins__) BIF=build in functions 内置函数