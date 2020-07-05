#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/20 23:26
# @Author : XXX
# @title ： 把二叉树打印成多行
# @Site : 
# @File : 把二叉树打印成多行.py
# @Software: PyCharm

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

'''
遍历每一层节点，记录每一层的值列表cur_val，同时记录每个节点的下一层节点nextLayer_node
'''
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if pRoot is None:
            return []
        result = []
        cur = [pRoot]
        while cur != []:
            cur_val = []
            nextLayer_node = []
            for node in cur:
                cur_val.append(node.val)
                if node.left:
                    nextLayer_node.append(node.left)
                if node.right:
                    nextLayer_node.append(node.right)
            result.append(cur_val)
            cur = nextLayer_node
        return result

if __name__ == '__main__':
    a = []
    if not a:
        print(1)
    if a is None:
        print(2)
    if a == []:
        print(3)


