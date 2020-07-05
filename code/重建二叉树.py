#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/8 17:39
# @Author : XXX
# @title ： 重建二叉树
# @Site : 
# @File : 重建二叉树.py
# @Software: PyCharm

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        if pre is None:
            return None
        root = TreeNode(pre[0])
        n = tin.index(root.val)
        root.left = self.reConstructBinaryTree(pre[1: n + 1], tin[:n])
        root.right = self.reConstructBinaryTree(pre[n + 1:], tin[n + 1:])
        return root

