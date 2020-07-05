#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/22 21:21
# @Author : XXX
# @title ： 机器人的运动范围
# @Site : 
# @File : 机器人的运动范围.py
# @Software: PyCharm

class Solution:
    def __init__(self):
        self.count = 0

    def movingCount(self, threshold, rows, cols):
        # write code here
        judge = [[False for i in range(cols)] for j in range(rows)]
        self.Movement(threshold, 0, 0, judge)
        return self.count

    def Movement(self, threshold, i, j, judge):
        if (i >= 0 and i < len(judge) and j >= 0 and j < len(judge[0])) and judge[i][j] == False and sum(
                list(map(int, str(i)))) + sum(list(map(int, str(j)))) <= threshold:
            judge[i][j] = True
            self.count += 1
            self.Movement(threshold, i - 1, j, judge)
            self.Movement(threshold, i + 1, j, judge)
            self.Movement(threshold, i, j + 1, judge)
            self.Movement(threshold, i, j - 1, judge)


if __name__ == '__main__':
    # a = map(int, str('123'))
    # print(list(a))
    # print([[False for i in range(3)] for j in range(3)])
    A = Solution()
    A.movingCount(15,20,20)
