#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/13 19:27
# @Author : XXX
# @title ： 二叉搜索树与双向链表
# @Site : 
# @File : 二叉搜索树与双向链表.py
# @Software: PyCharm

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.phead = None
        self.temp = None

    def Convert(self, pRootOfTree):
        # write code here
        if pRootOfTree is None:
            return None

        if self.phead is None:
            self.phead = pRootOfTree

        self.Convert(pRootOfTree.left)
        if pRootOfTree.left:
            if self.phead.val > pRootOfTree.left.val:
                self.phead = pRootOfTree.left
            self.temp = pRootOfTree.left
            self.temp.right = pRootOfTree

        else:
            if pRootOfTree.right:
                self.temp = pRootOfTree.right
                self.temp.left = pRootOfTree


        return self.phead

if __name__ == "__main__":
    s = Solution()
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(5)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(6)
    head = s.Convert(root)
    print(1)



