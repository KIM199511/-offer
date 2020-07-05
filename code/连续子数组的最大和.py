#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/14 11:13
# @Author : XXX
# @title ： 连续子数组的最大和
# @Site : 
# @File : 连续子数组的最大和.py
# @Software: PyCharm

class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        if len(array) == 0:
            return 0
        if len(array) == 1:
            return array[0]
        temp_array = [array[0]]
        for i in range(1,len(array)):
            sum_front = sum(array[:i])
            if sum_front < 0:
                temp_array.append(array[i])
            else:
                temp_array.append(temp_array[-1]+array[i])
        return max(temp_array)




if __name__ == '__main__':
    A = Solution()
    print(A.FindGreatestSumOfSubArray([1,-2,3,10,-4,7,2,-5]))

