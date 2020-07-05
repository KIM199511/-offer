#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/10 23:30
# @Author : XXX
# @title ： 链表中的倒数第K个节点
# @Site : 
# @File : 链表中的倒数第K个节点.py
# @Software: PyCharm

class Solution:
    def FindKthToTail(self, head, k):
        if not head or k < 0:
            return None
        f = s = head
        for i in range(k-1):
            f = f.next
            if f is None:
                return None
        while f.next is not None:
            f = f.next
            s = s.next
        return s