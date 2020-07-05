#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/11 19:16
# @Author : XXX
# @title ： 栈的压入、弹出序列
# @Site : 
# @File : 栈的压入、弹出序列.py
# @Software: PyCharm

class Solution:
    def IsPopOrder(self,pushV, popV):
        temp = []
        while pushV:
            for value in pushV:
                temp.append(value)
                while temp[-1] == popV[0]:
                    temp.pop()
                    popV.pop(0)
                    if popV == []:
                        return True
            return False

if __name__ == '__main__':
    A = Solution()
    a = [1,2,3,4,5]
    b = [4,5,3,2,1]
    print(A.IsPopOrder(a,b))
