#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/17 23:37
# @Author : XXX
# @title ： 左旋转字符串
# @Site : 
# @File : 左旋转字符串.py
# @Software: PyCharm

class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        length = len(s)
        if length == n:
            return s

        index_array = [value for value in range(length)]
        new_n = n
        if length < n:
            new_n = new_n % length
        new_index_array = [(value - new_n) for value in index_array]
        new_str = [""]*length
        for i in range(length):
            new_str[new_index_array[i]] = s[i]

        return "".join(new_str)

if __name__ == '__main__':
    s = "abcdefg"
    n = 2
    A = Solution()
    print(A.LeftRotateString(s,n))


