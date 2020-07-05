#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/14 12:59
# @Author : XXX
# @title ： 整数中1出现的次数（从1到n整数中1出现的次数
# @Site : 
# @File : 整数中1出现的次数（从1到n整数中1出现的次数.py
# @Software: PyCharm

class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        count = 0
        for i in range(1,n+1):
            temp = i
            while temp >= 1:
                if (int(temp) % 10) == 1:
                    count += 1
                temp /= 10
        return count

if __name__ == '__main__':
    A = Solution()
    A.NumberOf1Between1AndN_Solution(13)