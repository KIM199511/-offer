#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/16 11:16
# @Author : XXX
# @title ： 两个链表的第一个公共结点
# @Site : 
# @File : 两个链表的第一个公共结点.py
# @Software: PyCharm

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        if not pHead1 or not pHead2:
            return None
        ptr1 = pHead1
        ptr2 = pHead2
        while ptr1 != ptr2:
            if ptr1 == None:
                '''
                这个相当于走了一步
                '''
                ptr1 = pHead2
            else:
                ptr1 = ptr1.next
            if ptr2 == None:
                ptr2 = pHead1
            else:
                ptr2 = ptr2.next
        return ptr1

    def getIntersectionNode(self, headA, headB):
        p1, p2 = headA, headB
        while p1 is not p2:
            p1 = p1.next if p1 else headB
            p2 = p2.next if p2 else headA
        return p1


if __name__ == '__main__':
    s = Solution()
    common_node = ListNode(3)
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = common_node
    common_node.next = ListNode(4)
    common_node.next.next = ListNode(11)

    l2 = ListNode(9)
    l2.next = common_node

    s.getIntersectionNode(l1, l2)