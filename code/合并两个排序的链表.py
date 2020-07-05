#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/11 16:39
# @Author : XXX
# @title ： 合并两个排序的链表
# @Site : 
# @File : 合并两个排序的链表.py
# @Software: PyCharm

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        head = ListNode(None)
        head.next = None
        temp = head
        while pHead1 is not None and pHead2 is not None:
            if pHead1.val <= pHead2.val:
                head.next = pHead1
                # head = head.next
                pHead1 = pHead1.next
            else:
                head.next = pHead2
                # head = head.next
                pHead2= pHead2.next
            """优化代码"""
            head = head.next
        # if pHead1 is None:
        #     head.next = pHead2
        # if pHead2 is None:
        #     head.next = pHead1
        head.next = pHead1 or pHead2

        return temp.next

if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(3)
    c = ListNode(5)
    d = ListNode(2)
    e = ListNode(4)
    f = ListNode(6)
    a.next = b
    b.next = c
    c.next = None
    d.next = e
    e.next = f
    f.next = None
    s = Solution()
    s.Merge(a,d)
    print(None or 1)

