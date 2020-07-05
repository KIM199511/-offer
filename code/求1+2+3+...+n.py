#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/18 18:23
# @Author : XXX
# @title ： 求1+2+3+...+n
# @Site : 
# @File : 求1+2+3+...+n.py
# @Software: PyCharm

class Solution:
    def __init__(self):
        self.sum = 0
    def Sum_Solution(self, n):
        if n<=0:
            return 0
        self.getSum(n)
        return self.sum
    def getSum(self,n):
        self.sum+=n
        n = n - 1
        '''
        return a and b
 
        等价于
 
        return b if a else a
        '''
        return n>0 and self.getSum(n)




if __name__ == '__main__':
    n = 3
    A = Solution()
    # A.Sum_Solution(n)

