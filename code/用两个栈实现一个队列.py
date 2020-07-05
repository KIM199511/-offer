#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/9 14:52
# @Author : XXX
# @title ： 用两个栈实现一个队列
# @Site : 
# @File : 用两个栈实现一个队列.py
# @Software: PyCharm


class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self, node):
        self.stack1.append(node)
        print(self.stack1)

    def pop(self):
        return self.stack1.pop(0)

if __name__ == '__main__':
    a = Solution()
    print(a.stack1)
    a.push(1)
    a.push(2)
    print(a.pop())