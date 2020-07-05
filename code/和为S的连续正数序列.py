#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/17 14:10
# @Author : XXX
# @title ： 和为S的连续正数序列
# @Site : 
# @File : 和为S的连续正数序列.py
# @Software: PyCharm


class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here

        tsum_array = [i for i in range(1,tsum+1)]
        result = []
        pf = 1
        pb = 0
        while pb < pf and pf < tsum:
            Sum = (tsum_array[pb] + tsum_array[pf]) * (pf - pb + 1) / 2
            if Sum == tsum:
                result.append(tsum_array[pb:pf+1])
                pf += 1
            elif Sum < tsum:
                pf += 1
            elif Sum > tsum:
                pb += 1
        return result

if __name__ == '__main__':
    A = Solution()
    print(A.FindContinuousSequence(10))


