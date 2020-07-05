#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/13 11:09
# @Author : XXX
# @title ： 二叉搜索树的后序遍历序列
# @Site : 
# @File : 二叉搜索树的后序遍历序列.py
# @Software: PyCharm


class Solution:
    def VerifySquenceOfBST(self, sequence):
        if sequence == []:
            return False
        if len(sequence) <= 2:
            return True

        return self.A(sequence)



    def A(self, sequence):

        if len(sequence) <= 2:
            return True
        root = sequence.pop()
        if max(sequence) < root:
            return self.A(sequence)
        if min(sequence) > root:
            return self.A(sequence)
        index = None
        for i in range(len(sequence)):
            if sequence[i] > root:
                index = i
                break

        if sequence[:index] == [] or sequence[index:] == []:
            if sequence[:index] == [] and min(sequence[index:]) > root:
                return self.A(sequence[index:])
            elif sequence[index:] == [] and max(sequence[:index])<root:
                return self.A(sequence[:index])
            else:
                return False
        elif sequence[:index] != [] and  sequence[index:] != []:
            if max(sequence[:index])<root and min(sequence[index:]) > root:
                return self.A(sequence[:index]) and self.A(sequence[index:])
            else:
                return False

if __name__ == '__main__':
    w = Solution()
    flag = w.VerifySquenceOfBST([4,8,6,12,16,14,10])
    print(flag)