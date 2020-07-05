#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/9 23:29
# @Author : XXX
# @title ： 二进制中1的个数
# @Site : 
# @File : 二进制中1的个数.py
# @Software: PyCharm
class Solution:
    def NumberOf1(self, n):
        number = 0
        if n < 0:
            n = 0x7FFFFFFF & n
        while n:
            n = n & (n - 1)
            number += 1
        return number
