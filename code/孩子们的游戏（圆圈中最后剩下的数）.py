#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/18 20:14
# @Author : XXX
# @title ： 孩子们的游戏（圆圈中最后剩下的数）
# @Site : 
# @File : 孩子们的游戏（圆圈中最后剩下的数）.py
# @Software: PyCharm
class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        if n <= 0 or m <= 0:
            return -1

        pop_index = 0
        index_array = [i for i in range(n)]
        while len(index_array) > 1:
            pop_index = (m + pop_index - 1) % len(index_array)
            index_array.pop(pop_index)
        return index_array[0]


if __name__ == '__main__':
    n = 4
    m = 2
    A = Solution()
    print(A.LastRemaining_Solution(n, m))
