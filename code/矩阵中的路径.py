#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/22 16:57
# @Author : XXX
# @title ： 矩阵中的路径
# @Site : 
# @File : 矩阵中的路径.py
# @Software: PyCharm
class Solution:
    def dfs(self,matrix,flag,rows,cols,r,c,s):
        if s=='':
            return True
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]   # 利用两个数组，来实现对每个格子周围格子的访问
        for k in range(4):
            x = dx[k] + r
            y = dy[k] + c
            if x >= 0 and x < rows and y >= 0 and y < cols and flag[x][y] and matrix[x*cols+y]==s[0]:
                flag[x][y]=False   # 修改当前格子的标识
                if self.dfs(matrix,flag[:],rows,cols, x, y,s[1:]):   # 递归
                    return True
                flag[x][y]=True
                # 如果上一个判断条件返回的是False，那么就说明这个格子目前还不是路径上的格子，再把当前格子的标识修改回来。
        return False
    def hasPath(self, matrix, rows, cols, path):
        if path == '':
            return True
        flag = [[True for c in range(cols)] for r in range(rows)]  # 定义一个表示矩阵
        for r in range(rows):
        # 对这个矩阵中的元素进行遍历，不断找路径进入矩阵的起点，直到以某个格子为起点找到整个路径为止。
            for c in range(cols):
                if matrix[r*cols+c] == path[0]:
                    flag[r][c] = False
                    if self.dfs(matrix,flag[:],rows,cols, r, c,path[1:]):
                        return True
                    flag[r][c] = True
        return False
