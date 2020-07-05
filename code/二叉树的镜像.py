#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/11 18:13
# @Author : XXX
# @title ： 二叉树的镜像
# @Site : 
# @File : 二叉树的镜像.py
# @Software: PyCharm


class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        if root != None:
            root.left, root.right = root.right, root.left
            self.Mirror(root.left)
            self.Mirror(root.right)
        else:
            return None

