#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/18 20:45
# @Author : XXX
# @title ： 不用加减乘除做加法
# @Site : 
# @File : 不用加减乘除做加法.py
# @Software: PyCharm
class Solution:
    def Add(self, num1, num2):
        while num2!=0:
            sum = num1^num2
            carry = (num1&num2)<<1
            num1 = sum
            num2 = carry
        return num1