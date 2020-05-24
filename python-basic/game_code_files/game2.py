#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 打飞机小游戏框架逻辑
""""
    1.加载背景音乐-单曲循环
    2.初始化我方飞机
    3.
        while True:
        if '用户是否点击关闭按钮':
            "退出程序"
        小飞机三生
        小飞机移动一个位置
        屏幕刷新

        if 用户鼠标移动：
            我方飞机中心位置 = 用户鼠标位置
            屏幕刷新

        if 我方飞机与小飞机发生碰撞：
            我方失败，播放失败音乐
            修改我方飞机图案
            打印 "game over"
            停止背景音乐淡出播放


"""

# 时间间隔
interval = 0

while True:

    interval +=1
    if interval == 50:
        interval = 0


