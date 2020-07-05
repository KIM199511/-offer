#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/18 10:14
# @Author : XXX
# @title ： 扑克牌顺子
# @Site : 
# @File : 扑克牌顺子.py
# @Software: PyCharm

class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if not numbers or numbers == []:
            return False
        joker = 0
        need = 0
        sorted_numbers = sorted(numbers)
        for i in range(len(sorted_numbers)):
            if sorted_numbers[i] == 0:
                joker += 1

        if len(numbers[joker:]) != len(list(set(numbers[joker:]))):
            return False

        for i in range(joker,len(sorted_numbers)-1):
            if (sorted_numbers[i] + 1) != sorted_numbers[i+1]:
                need += (sorted_numbers[i+1] - sorted_numbers[i] - 1)

        if joker >= need:
            return True
        else:
            return False


