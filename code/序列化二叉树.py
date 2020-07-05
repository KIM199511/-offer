#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/22 15:02
# @Author : XXX
# @title ： 序列化二叉树
# @Site : 
# @File : 序列化二叉树.py
# @Software: PyCharm

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def Serialize(self, root):
        # write code here 中序遍历
        if root is None:
            return '#'
        return root.val+','+self.Serialize(root.left)+','+self.Serialize(root.right)

    def Deserialize(self, s):
        # write code here
        s_list = s.split(',')
        return self.deserialize(s_list)

    def deserialize(self, s_list):
        if len(s_list) <= 0:
            return None
        val = list.pop(0)
        root = None
        if val != '#':
            root = TreeNode(int(val))
            root.left = self.deserialize(s_list)
            root.right = self.deserialize(s_list)
        return root
