#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/8 17:16
# @Author : XXX
# @title ： 替换空格
# @Site : 
# @File : 替换空格.py
# @Software: PyCharm

class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        new_s = ""
        for char in s:
            if char == " ":
                new_s += "%20"
            else:
                new_s += char
        return new_s