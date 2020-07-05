#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/20 12:38
# @Author : XXX
# @title ： 字符流中第一个不重复的字符
# @Site : 
# @File : 字符流中第一个不重复的字符.py
# @Software: PyCharm

class Solution:
    # 返回对应char
    def __init__(self):
        self.str = ""
        self.dic = {}

    def FirstAppearingOnce(self):
        # write code here
        for value in self.str:
            if self.dic[value] == 1:
                return value
        return '#'

    def Insert(self, char):
        # write code here
        self.str += char
        if char in self.dic:
            self.dic[char] += 1
        else:
            self.dic[char] = 1