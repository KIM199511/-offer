#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/20 16:19
# @Author : XXX
# @title ： 对称的二叉树
# @Site : 
# @File : 对称的二叉树.py
# @Software: PyCharm


# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        if pRoot is None:
            return True
        return self.isSymmetrical_part(pRoot.left,pRoot.right)


    def isSymmetrical_part(self, leftRoot, rightRoot):
        if leftRoot is None and rightRoot is None:
            return True
        if leftRoot is None or rightRoot is None or leftRoot.val != rightRoot.val:
            return False

        return self.isSymmetrical_part(leftRoot.left,rightRoot.right) and self.isSymmetrical_part(leftRoot.right,rightRoot.left)

