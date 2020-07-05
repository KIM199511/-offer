#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/9 16:15
# @Author : XXX
# @title ： 动态规划跳台阶
# @Site : 
# @File : 动态规划跳台阶.py
# @idea : 动态规划 Fn = Fn-1 + Fn-2
# @Software: PyCharm

# class Solution:
#     def jumpFloor(self, number):
#         if number > 2:
#             return self.jumpFloor(number-1)+self.jumpFloor(number-2)
#         elif number == 0:
#             return 0
#         elif number == 1:
#             return 1
#         elif number == 2:
#             return 2

class Solution:
    def jumpFloor(self, number):
        if number == 0:
            return 0
        elif number == 1:
            return 1
        elif number == 2:
            return 2
        elif number > 2:
            a = 1
            b = 2
            for i in range(number-2):
                a,b = b,a+b
        return b

if __name__ == '__main__':
    a = Solution()
    print(a.jumpFloor(4))

