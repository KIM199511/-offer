#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/11 18:52
# @Author : XXX
# @title ： 顺时针打印矩阵
# @Site : 
# @File : 顺时针打印矩阵.py
# @Software: PyCharm

'''
数组在python中，[]不能用is None判断，只能通过长度以及==[]判断
'''

class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        result = []
        while matrix:
            result += matrix.pop(0)
            if matrix == [] :
                return result
            matrix = self.turn(matrix)
        pass
    def turn(self,matrix):
        num_r = len(matrix)
        num_c = len(matrix[0])
        newmat = []
        for i in range(num_c):
            newmat2 = []
            for j in range(num_r):
                newmat2.append(matrix[j][i])
            newmat.append(newmat2)
        newmat.reverse()
        return newmat

if __name__ == '__main__':
    a = [[1]]
    A = Solution()
    A.printMatrix(a)


