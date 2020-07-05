#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/11 17:15
# @Author : XXX
# @title ： 树的子结构
# @Site : 
# @File : 树的子结构.py
# @Software: PyCharm

'''
思路：采用递归的思路，单独定义一个函数判断B是不是从当前A的
根节点开始的子树，这里判断是不是子树也需要一个递归的判断。
如果是，则返回True，如果不是，再判断B是不是从当前A的根节点
的左子节点或右子节点开始的子树。
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        if pRoot1 is None or pRoot2 is None:
            return False
        """
        根结点满足，且子树相同才能为子树结构  核心！！！
        """
        if pRoot1.val == pRoot2.val and self.isSubtree(pRoot1.left , pRoot2.left) and self.isSubtree(pRoot1.right, pRoot2.right):
                return True
        else:
            return self.HasSubtree(pRoot1.left , pRoot2) or self.HasSubtree(pRoot1.right, pRoot2)

    def isSubtree(self,pRoot1, pRoot2):
        if pRoot2 is None:
            return True
        if pRoot1 is None and pRoot2 is not None:
            return False
        if pRoot1.val == pRoot2.val:
            return self.isSubtree(pRoot1.left, pRoot2.left) and self.isSubtree(pRoot1.right, pRoot2.right)
        if pRoot1.val != pRoot2.val:
            return False

if __name__ == '__main__':
    a = TreeNode(8)
    b = TreeNode(8)
    c = TreeNode(7)
    d = TreeNode(9)
    e = TreeNode(2)
    f = TreeNode(4)
    g = TreeNode(7)
    x = TreeNode(8)
    y = TreeNode(9)
    z = TreeNode(2)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    d.right = None
    d.left = None
    e.left =None
    e.right = None
    c.left = f
    c.right = g
    x.left = y
    x.right = z
    y.left = None
    y.right = None
    z.right = None
    z.left = None
    A = Solution()
    g = A.HasSubtree(a,x)
    g=1




