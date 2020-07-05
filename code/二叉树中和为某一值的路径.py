#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/13 12:05
# @Author : XXX
# @title ： 二叉树中和为某一值的路径
# @Site : 
# @File : 二叉树中和为某一值的路径.py
# @Software: PyCharm

class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        if root is None:
            return []
        self.array = []
        self.subPath(root, [], expectNumber)
        return self.array


    def subPath(self, root, path, expectNumber):
        if root.left is None and root.right is None:
            if expectNumber == root.val:
                self.array.append(path + [root.val])
        if root.left:
            self.subPath(root.left, path + [root.val], expectNumber - root.val)
        if root.right:
            self.subPath(root.right, path + [root.val], expectNumber - root.val)
