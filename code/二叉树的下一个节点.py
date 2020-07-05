#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/20 15:52
# @Author : XXX
# @title ： 二叉树的下一个节点
# @Site : 
# @File : 二叉树的下一个节点.py
# @Software: PyCharm

# -*- coding:utf-8 -*-
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    def GetNext(self, pNode):
        if pNode is None:
            return None

        '''
        存在右子树
        '''
        if pNode.right:
            node = pNode.right
            while node.left:
                node = node.left
            return node

        '''
        不存在右子树
        '''
        while pNode.next:
            temp = pNode.next
            if temp.left == pNode:
                return temp
            else:
                pNode = temp
        return None





