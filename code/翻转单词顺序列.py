#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/18 10:02
# @Author : XXX
# @title ： 翻转单词顺序列
# @Site : 
# @File : 翻转单词顺序列.py
# @Software: PyCharm

class Solution:
    def ReverseSentence(self, s):
        # write code here
        s_array = []
        reversed_s = ""
        for value in s.split(" "):
            s_array.append(value)
        while s_array:
            reversed_s += (s_array.pop() + " ")
        return reversed_s[:-1]

if __name__ == '__main__':
    s = "student. a am I"
    A = Solution()
    print(A.ReverseSentence(s))

