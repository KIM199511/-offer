#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/13 19:13
# @Author : XXX
# @title ： 复杂链表的复制
# @Site : 
# @File : 复杂链表的复制.py
# @Software: PyCharm

class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        if pHead is None:
            return None

        newhead = RandomListNode(pHead.label)
        '''
        可以把random也看成节点一个属性
        '''
        newhead.random = pHead.random
        newhead.next = self.Clone(pHead.next)
        return newhead


