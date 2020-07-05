#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/10 0:03
# @Author : XXX
# @title ： 调整数组顺序使奇数位于偶数前面
# @Site : 
# @File : 调整数组顺序使奇数位于偶数前面.py
# @Software: PyCharm

class Solution:
    def reOrderArray(self, array):
        odd_array = []
        even_array = []
        for value in array:
            if value % 2 == 0:
                even_array.append(value)
            else:
                odd_array.append(value)
                odd_array.extend(even_array)
        return odd_array

if __name__ == '__main__':
    a = Solution()
    print(a.reOrderArray([1,2,3,4,5,6,7]))


