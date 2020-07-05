#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/8 16:14
# @Author : XXX
# @title ： 二维数组中的查找
# @Site : 
# @File : 二维数组中的查找.py
# @Software: PyCharm

array = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
target = 16


class Solution:
    def Find(self, target, array):
        rows = len(array)
        cols = len(array[0])
        i = 0
        j = cols - 1
        while (  rows > i and 0 <= j):
            if target > array[i][j]:
                i += 1
                continue
            if target < array[i][j]:
                j -= 1
                continue
            if target == array[i][j]:
                return True
        return False


if __name__ == '__main__':
    a = Solution()
    print(a.Find(target, array))
