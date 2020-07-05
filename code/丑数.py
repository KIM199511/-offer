#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/15 9:53
# @Author : XXX
# @title ： 丑数
# @Site : 
# @File : 丑数.py
# @Software: PyCharm


class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index == 0:
            return 0
        if index == 1:
            return 1

        array = [1]
        two_array = []
        three_array = []
        five_array = []
        for i in range(index-1):
            base = array[-1]
            two_array.append(base*2)
            three_array.append(base*3)
            five_array.append(base*5)
            min_num = min(two_array[0],three_array[0],five_array[0])
            array.append(min_num)

            if min_num == two_array[0]:
                two_array.pop(0)
            if min_num == three_array[0]:
                three_array.pop(0)
            if min_num == five_array[0]:
                five_array.pop(0)
        return array[-1]

if __name__ == '__main__':
    A = Solution()
    print(A.GetUglyNumber_Solution(5))

