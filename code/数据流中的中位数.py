#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/22 15:40
# @Author : XXX
# @title ： 数据流中的中位数
# @Site : 
# @File : 数据流中的中位数.py
# @Software: PyCharm


class Solution:
    def __init__(self):
        self.data = []
    def Insert(self, num):
        # write code here
        self.data.append(num)
        self.data.sort()
    def GetMedian(self):
        # write code here
        length = len(self.data)
        if length % 2 == 0:
            return (self.data[length//2]+self.data[length//2-1])/2
        else:
            return self.data[length//2]