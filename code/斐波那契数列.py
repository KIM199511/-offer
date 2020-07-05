#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/9 16:01
# @Author : XXX
# @title ： 斐波那契数列
# @Site : 
# @File : 斐波那契数列.py
# @Software: PyCharm

class Solution:
    def Fibonacci(self,n):
        a = 1
        b = 1
        if n <= 0:
            return 0
        if n == 1 or n == 2:
            return 1
        else:
            for i in range(n-2):
                temp = b
                b = a+b
                a = temp
        return b

if __name__ == '__main__':
    a = Solution()
    a.Fibonacci(4)