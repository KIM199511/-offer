#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/17 12:38
# @Author : XXX
# @title ： 二叉树的深度
# @Site : 
# @File : 二叉树的深度.py
# @Software: PyCharm

class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

class Solution:
     def TreeDepth(self, pRoot):
        if pRoot is None:
            return 0
        else:
            return max(self.TreeDepth(pRoot.left), self.TreeDepth(pRoot.left)) + 1

if __name__ == '__main__':
    s = Solution()
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    e = TreeNode(5)
    a.left = b
    b.left = c
    c.left = d
    d.left = e

    print(s.TreeDepth(a))
    # print(s1.isBalanceTree(root))