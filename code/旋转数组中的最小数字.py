#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/8 23:41
# @Author : XXX
# @title ： 旋转数组中的最小数字
# @Site : 
# @File : 旋转数组中的最小数字.py
# @Software: PyCharm

class Solution:
    def minNumberInRotateArray(self, rotateArray):
        if rotateArray is None:
            return 0
        f = 0
        l = len(rotateArray) - 1
        while f < l:
            mid = (f + l) / 2
            if rotateArray[mid] > rotateArray[l]:
                f = mid + 1
            else:
                l = mid
            return rotateArray[f]
