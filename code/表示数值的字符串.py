#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/20 12:17
# @Author : XXX
# @title ： 表示数值的字符串
# @Site : 
# @File : 表示数值的字符串.py
# @Software: PyCharm
import re
class Solution:
     # s字符串
     def isNumeric(self, s):
         # write code here
         pattern = re.compile("[\\+\\-]?\\d*(\\.\\d+)?([eE][\\+\\-]?\\d+)?")
         return pattern.match(s).group(0)==s
