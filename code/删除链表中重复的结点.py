#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/20 13:19
# @Author : XXX
# @title ： 删除链表中重复的结点
# @Site : 
# @File : 删除链表中重复的结点.py
# @Software: PyCharm

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplication(self, pHead):
        head = ListNode(None)
        head.next = pHead
        fast = pHead
        slow = head
        while fast:
            if fast.next is not None:
                if fast.next.val != fast.val:
                    slow.next = fast
                    slow = slow.next
                else:
                    while fast.next is not None and fast.next.val == fast.val:
                        fast = fast.next
                fast = fast.next
            else:
                slow.next = fast
                return head.next
        slow.next = fast
        return head.next


        # while pHead.val == repeat[0]:
        #     if pHead.next:
        #         pHead = pHead.next
        #         repeat.pop(0)
        #     else:
        #         return None
        #
        # f = pHead
        # s = pHead
        # while f:
        #     while  f.val == repeat[0]:
        #         repeat.pop(0)
        #         f = f.next
        #     else:
        #         s.next = f
        #         s = s.next
        # return pHead







if __name__ == '__main__':
    a1 = ListNode(1)
    a2 = ListNode(1)
    a3 = ListNode(1)
    a4 = ListNode(1)
    a5 = ListNode(1)
    a6 = ListNode(1)
    a7 = ListNode(1)
    a1.next = a2
    a2.next = a3
    a3.next = a4
    a4.next = a5
    a5.next = a6
    a6.next = a7

    A = Solution()
    A.deleteDuplication(a1)
