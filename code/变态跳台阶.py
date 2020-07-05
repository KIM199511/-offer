#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/9 19:40
# @Author : XXX
# @title ： 变态跳台阶
# @Site : 
# @File : 变态跳台阶.py
# @Software: PyCharm

class Solution:
    def jumpFloorII(self, number):
        # write code here
        if number <= 0:
            return 0
        if number == 1:
            return 1
        if number >= 2:
            a = 1
            for i in range(number - 1):
                a = 2 * a
            return a

if __name__ == '__main__':
    a = Solution()
    print(a.jumpFloorII(3))

