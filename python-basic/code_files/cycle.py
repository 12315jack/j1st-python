#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 循环使用

'''
    使用循环 获取学生的分数等级
    90-100 A
    80-90 B
    70-80 C
    60-70 D
    < 60 不及格
    > 100 输入有错
'''

score = int(input("请输入学生的成绩："))

if 90 <= score <=100:
    print('A')
elif 80 <= score < 90:
    print('B')
elif 70 <= score < 80:
    print('C')
elif 60 <= score < 70:
    print('D')
elif score > 100:
    print("输入有错")
else:
    print("成绩不合格或者")


# 三元操作符
x,y=6,9
if x<y:
    small=x
else:
    small=y

print(small)

print(x if x < y else y)