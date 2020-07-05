#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/22 16:29
# @Author : XXX
# @title ： 滑动窗口的最大值
# @Site : 
# @File : 滑动窗口的最大值.py
# @Software: PyCharm

# class Solution:
#     def maxInWindows(self, num, size):
#         # write code here
#         if size > len(num):
#             return None
#         times = size - len(num) + 1
#         result = []
#         for i in range(times):
#             temp = []
#             temp.extend(num[:i])
#             temp.append(num[i:i+size])
#             temp.extend(num[i+size])
#             result.append(temp)
#         return result

class Solution:
    def maxInWindows(self, num, size):
        # write code here
        if size > len(num) or size == 0:
            return []
        times = len(num) - size + 1
        result = []
        for i in range(times):
            temp = max(num[i:i+size])
            result.append(temp)
        return result


if __name__ == '__main__':
    a = [1,2,3]
    a = a[:0]
    a.extend([1,2])
    print(a)
    A = Solution()
    print(A.maxInWindows([2,3,4,2,6,2,5,1],3))

