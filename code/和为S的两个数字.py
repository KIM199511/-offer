#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/17 15:28
# @Author : XXX
# @title ： 和为S的两个数字
# @Site : 
# @File : 和为S的两个数字.py
# @Software: PyCharm

class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        if array == []:
            return []
        ph = 0
        pt = len(array) - 1
        Sum = array[ph] + array[pt]
        while Sum != tsum and pt > ph:
            if Sum > tsum:
                pt -= 1
            if Sum < tsum:
                ph += 1
            Sum = array[ph] + array[pt]
        if Sum == tsum:
            return [array[ph],array[pt]]
        return []

if __name__ == '__main__':
    array = [1,3,5,6,9]
    s = 9
    A = Solution()
    print(A.FindNumbersWithSum(array,s))




