#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/19 16:33
# @Author : XXX
# @title ： 把字符串转换成整数
# @Site : 
# @File : 把字符串转换成整数.py
# @Software: PyCharm

class Solution:
    def StrToInt(self, s):
        # write code here
        length = len(s)
        if length == 0:
            return 0
        if length == 1:
            if (s[0] >="0" and s[0]<="9"):
                return int(s)
            else:
                return 0

        flag = 1
        if s[0] == "+":
            s = s[1:]

        if s[0] == "-":
            s = s[1:]
            flag = 0

        if (s[0] <="0" and s[0]>="9"):
            return 0


        for i in range(len(s)):
            if s[i] >="0" and s[i]<="9":
                continue
            else:
                return 0

        Sum = 0
        base = 1
        for i in range(len(s)-1,-1,-1):
            Sum += (int(s[i]) * base)
            base *= 10
        if flag == 1:
            return Sum
        elif flag == 0:
            return - Sum


if __name__ == '__main__':
    A = Solution()
    # print(A.StrToInt("+2147483647"))
    print(A.StrToInt('1a33'))

