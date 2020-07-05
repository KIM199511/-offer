#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/14 10:52
# @Author : XXX
# @title ： 最小的K个数
# @Site : 
# @File : 最小的K个数.py
# @Software: PyCharm

class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        if k > len(tinput):
            return []
        put_array = self.Sort(tinput)
        return put_array[:k]


    def Sort(self,array):
        if len(array) < 2:
            return array

        prov = array[0]
        left_array = []
        right_array = []
        for value in array[1:]:
            if value > prov:
                right_array.append(value)
            else:
                left_array.append(value)
        return self.Sort(left_array)+[prov]+self.Sort(right_array)

if __name__ == '__main__':
    A = Solution()
    L = A.GetLeastNumbers_Solution([3,2,4,1],2)
    print(L)


