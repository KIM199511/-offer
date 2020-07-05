#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/15 11:27
# @Author : XXX
# @title ： 第一个只出现一次的字符
# @Site : 
# @File : 第一个只出现一次的字符.py
# @Software: PyCharm
class Solution:
    def FirstNotRepeatingChar(self, s):
        hash_list = [0] * 256
        for char in s:
            hash_list[ord(char)] += 1
        for char in s:
            if hash_list[ord(char)] == 1:
                return s.index(char)
        return -1
if __name__ == '__main__':
    s = "aabcc"
    A = Solution()
    print(A.FirstNotRepeatingChar("GOOGLR"))