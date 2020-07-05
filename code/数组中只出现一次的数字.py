#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/17 13:46
# @Author : XXX
# @title ： 数组中只出现一次的数字
# @Site : 
# @File : 数组中只出现一次的数字.py
# @Software: PyCharm
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        base = array[0]
        for num in range(1, len(array)):
            base = base ^ array[num]

        temp = 0
        while base % 2 != 1:
            temp += 1
            base = base >> 1

        array1 = []
        array2 = []
        for value in array:
            if (value>>temp) % 2 == 1:
                array1.append(value)
            else:
                array2.append(value)

        base1 = array1[0]
        for num in range(1, len(array1)):
            base1 = base1 ^ array1[num]
        base2 = array2[0]
        for num in range(1, len(array2)):
            base2 = base2 ^ array2[num]

        return base1,base2

if __name__ == '__main__':
    A = Solution()
    print(A.FindNumsAppearOnce([1,2,2,3]))
