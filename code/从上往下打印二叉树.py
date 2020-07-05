#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/11 23:38
# @Author : XXX
# @title ： 从上往下打印二叉树
# @Site : 
# @File : 从上往下打印二叉树.py
# @Software: PyCharm

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def PrintFromTopToBottom(self, root):
        if root is None:
            return []
        '''
        PYTHON深浅拷贝
        '''
        final_list = [root]
        node_list = [root]
        while node_list != []:
            node_list = self.RootList(node_list)
            final_list += node_list

        array = []
        for value in final_list:
            array.append(value.val)
        return array

        # temp.append(self.PrintFromTopToBottom(root.left))
        # temp.append(self.PrintFromTopToBottom(root.right))

    def RootList(self,node_list):
        length = len(node_list)
        for i in range(length):
            if node_list[0].left is not None:
                node_list.append(node_list[0].left)
            if node_list[0].right is not None:
                node_list.append(node_list[0].right)
            node_list.pop(0)
        return node_list

if __name__ == '__main__':
    a = TreeNode(10)
    b = TreeNode(6)
    c = TreeNode(14)
    a.left = b
    a.right = c
    A = Solution()
    print(A.PrintFromTopToBottom(None))
