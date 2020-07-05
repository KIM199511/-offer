#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/21 23:31
# @Author : XXX
# @title ： 二叉搜索树的第k个结点
# @Site : 
# @File : 二叉搜索树的第k个结点.py
# @Software: PyCharm

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回对应节点TreeNode
    def __init__(self):
        self.node_list = []

    def Tree2List(self, pRoot):
        # write code here
        if pRoot is None:
            return None

        if pRoot.left:
            self.Tree2List(pRoot.left)

        self.node_list.append(pRoot)

        if pRoot.right:
            self.Tree2List(pRoot.right)

    def KthNode(self, pRoot, k):
        self.Tree2List(pRoot)
        if k <= 0 or k > len(self.node_list):
            return None
        return self.node_list[k-1]