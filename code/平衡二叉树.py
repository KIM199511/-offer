#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/17 13:39
# @Author : XXX
# @title ： 平衡二叉树
# @Site : 
# @File : 平衡二叉树.py
# @Software: PyCharm

class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        if pRoot is None:
            return True
        if abs(self.Tree_Length(pRoot.left) - self.Tree_Length(pRoot.right)) < 2:
            return True
        else:
            return False

    def Tree_Length(self,root):
        if root is None:
            return 0
        else:
            return max(self.Tree_Length(root.left),self.Tree_Length(root.right)) + 1


