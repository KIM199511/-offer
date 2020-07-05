#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/9 23:52
# @Author : XXX
# @title ： 数值的整数次方
# @Site : 
# @File : 数值的整数次方.py
# @Software: PyCharm

class Solution:
    def Power(self, base, exponent):
        abs = 1
        power_value = 1
        if base == 0:
            return 0
        elif exponent == 0:
            return 1

        if exponent < 0:
            exponent = -exponent
            abs = 0

        while exponent != 0:
            power_value = power_value * base
            exponent -= 1

        if abs == 1:
            return power_value
        elif abs == 0:
            return 1 / power_value

if __name__ == '__main__':
    a = Solution()
    print(a.Power(-2,3))