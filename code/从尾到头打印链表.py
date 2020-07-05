#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/8 17:21
# @Author : XXX
# @title ： 从尾到头打印链表
# @Site : 
# @File : 从尾到头打印链表.py
# @Software: PyCharm

class Solution:
    def printListFromTailToHead(self, listNode):
        if listNode is None:
            return []
        ptr = listNode
        stack = []
        while ptr:
            stack.append(ptr.val)
            ptr = ptr.next
        return list(reversed(stack))

a = [1,2,3]
print(list(reversed(a)))