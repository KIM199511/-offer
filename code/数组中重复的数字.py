#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/19 17:12
# @Author : XXX
# @title ： 数组中重复的数字
# @Site : 
# @File : 数组中重复的数字.py
# @Software: PyCharm

class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        array = []
        for i in range(numbers):
            array.append(duplication[i])
            if len(list(set(array))) < len(array):
                duplication[0] = duplication[i]
                return True
        return False

