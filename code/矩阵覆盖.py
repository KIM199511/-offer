#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/9 23:06
# @Author : XXX
# @title ： 矩阵覆盖
# @Site : 
# @File : 矩阵覆盖.py
# @Software: PyCharm

class Solution:
    def rectCover(self, number):
        if number <= 0:
            return 0
        if number == 1:
            return 1
        if number >= 2:
            a = 1
            b = 1
            for i in range(number - 1):
                a,b = b, a+b
        return b

if __name__ == '__main__':
    a = Solution()
    print(a.rectCover(3))
