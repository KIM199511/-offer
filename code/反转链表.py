#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/10 23:52
# @Author : XXX
# @title ： 反转链表
# @Site : 
# @File : 反转链表.py
# @Software: PyCharm

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        if pHead is None or pHead.next is None:
            return pHead
        pf = pHead
        pb = pHead.next
        pHead.next = None
        while pb is not None:
            temp = pb.next
            pb.next = pf
            pf = pb
            pb = temp
        return pf

if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    a.next = b
    b.next = c
    c.next = None
    s = Solution()
    s.ReverseList(a)


