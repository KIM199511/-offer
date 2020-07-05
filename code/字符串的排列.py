#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/13 22:41
# @Author : XXX
# @title ： 字符串的排列
# @Site : 
# @File : 字符串的排列.py
# @Software: PyCharm
class Solution:
    def Permutation(self,ss):
        if ss == '':
            return []
        return sorted(list(set(self.Permutation_support(ss,[]))))


    def Permutation_support(self, ss,array):
        length = len(ss)
        if length <= 1:
            return [ss]
        for i in range(length):
            temp_array = self.Permutation(ss[:i]+ss[i+1:])
            for value in temp_array:
                array.append(ss[i] + value)
        return array

if __name__ == '__main__':
    # ss = "abc"
    # A = Solution()
    # l = A.Permutation(ss)
    # print(l)
    l = ["bb","aa","aa"]
    print(sorted(list(set(l))))

