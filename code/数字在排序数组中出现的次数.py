#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/16 13:07
# @Author : XXX
# @title ： 数字在排序数组中出现的次数
# @Site : 
# @File : 数字在排序数组中出现的次数.py
# @Software: PyCharm


class Solution:
    def GetNumberOfK(self, data, k):
        if len(data) == 0:
            return 0
        length = len(data)
        count = 0
        start = None
        if k > data[-1] or k < data[0]:
            return count
        for i in range(length):
            if data[i] == k:
                count += 1
                start = i
                break
            if data[i] > k:
                return count

        while start+1 < length and data[start+1] == k:
            count += 1
            start += 1
        return count






if __name__ == '__main__':
    A = Solution()
    print(A.GetNumberOfK([1,2,3,3,3,3,4,5],3))