#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/20 23:50
# @Author : XXX
# @title ： 按之字形顺序打印二叉树
# @Site : 
# @File : 按之字形顺序打印二叉树.py
# @Software: PyCharm

class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if pRoot is None:
            return []
        result = []
        cur = [pRoot]
        direction = 0
        while cur != []:
            cur_val = []
            nextLayer_node = []
            for node in cur:
                cur_val.append(node.val)
                if node.left:
                    nextLayer_node.append(node.left)
                if node.right:
                    nextLayer_node.append(node.right)

            if direction % 2 != 0:
                cur_val.reverse()
            result.append(cur_val)
            cur = nextLayer_node
            direction += 1
        return result

if __name__ == '__main__':
    a = [1,2,3]
    a.reverse()
    print(a[:,-1])