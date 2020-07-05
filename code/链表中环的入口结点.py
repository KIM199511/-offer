#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/20 12:46
# @Author : XXX
# @title ： 链表中环的入口结点
# @Site : 
# @File : 链表中环的入口结点.py
# @Software: PyCharm

'''
思路：快慢指针，快指针一次走两步，慢指针一次走一步。如果链表中存在环
，且环中假设有n个节点，那么当两个指针相遇时，快的指针刚好比慢的指针
多走了环中节点的个数，即n步。从另一个角度想，快的指针比慢的指针多走了
慢的指针走过的步数，也是n步。相遇后，快指针再从头开始走，快慢指针再
次相遇时，所指位置就是入口。


两个结论：
1、设置快慢指针，假如有环，他们最后一定相遇。
2、两个指针分别从链表头和相遇点继续出发，每次走一步，最后一定相遇与环入口。
证明结论1：设置快慢指针fast和low，fast每次走两步，low每次走一步。假如有环，两者一定会相遇（因为low一旦进环，
可看作fast在后面追赶low的过程，每次两者都接近一步，最后一定能追上）。
证明结论2：
设：
链表头到环入口长度为--a
环入口到相遇点长度为--b
相遇点到环入口长度为--c

链接：https://www.nowcoder.com/questionTerminal/253d2c59ec3e4bc68da16833f79a38e4?f=discussion
来源：牛客网

则：相遇时
快指针路程=a+(b+c)k+b ，k>=1  其中b+c为环的长度，k为绕环的圈数（k>=1,即最少一圈，不能是0圈，不然和慢指针走的一样长，矛盾）。
慢指针路程=a+b
快指针走的路程是慢指针的两倍，所以：
（a+b）*2=a+(b+c)k+b
化简可得：
a=(k-1)(b+c)+c 这个式子的意思是： 链表头到环入口的距离=相遇点到环入口的距离+（k-1）圈环长度。
其中k>=1,所以k-1>=0圈。所以两个指针分别从链表头和相遇点出发，最后一定相遇于环入口。
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def EntryNodeOfLoop(self, pHead):
        if  pHead==None or pHead.next==None or pHead.next.next == None:
            return None
        fast = pHead.next.next
        slow = pHead.next

        while fast != slow:
            if fast.next == None or fast.next.next == None:
                return None
            slow = slow.next
            fast = fast.next.next

        '''
        此时存在环，且 fast=slow在环中的相遇点
        '''
        fast = pHead
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return fast
