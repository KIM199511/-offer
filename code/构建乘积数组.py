#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/19 17:50
# @Author : XXX
# @title ： 构建乘积数组
# @Site : 
# @File : 构建乘积数组.py
# @Software: PyCharm

class Solution:
    def multiply(self, A):
        # write code here
        B = []
        B1 = []
        B2 = []
        length = len(A)
        for i in range(0, length):
            if i == 0:
                B1.append(1)
                B2.append(1)
            else:
                B1.append(B1[i - 1] * A[i - 1])
                B2.insert(0, B2[0] * A[length - i])

        for i in range(length):
            B.append(B1[i]*B2[i])
        return B

if __name__ == '__main__':
    A=Solution()
    print(A.multiply([1,2,3,4]))
