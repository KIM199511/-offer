#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/15 13:02
# @Author : XXX
# @title ： 数组中的逆序对
# @Site : 
# @File : 数组中的逆序对.py
# @Software: PyCharm



class Solution:
    '''
    更好一点的是拷贝该数组后对拷贝的数组排序。
    计算数组中的最小值在原始数组中出现的位置，
    统计原始数组中最小值前面的个数，之后在原始
    数组中去掉最小值。重复上述步骤。
    '''
    def InversePairs(self, data):
        # write code here
        copy_data = data
        count = 0
        copy_data = sorted(copy_data)
        for value in copy_data:
            index = data.index(value)
            count += index
            data.remove(value)

        return count % 1000000007




if __name__ == '__main__':
    A = Solution()
    s = [1,2,3,4,5,6,7,0]
    L = [364,637,341,406,747,995,234,971,571,219,993,407,416,366,315,301,601,650,418,355,460,505,360,965,516,648,727,667,465,849,455,181,486,149,588,233,144,174,557,67,746,550,474,162,268,142,463,221,882,576,604,739,288,569,256,936,275,401,497,82,935,983,583,523,697,478,147,795,380,973,958,115,773,870,259,655,446,863,735,784,3,671,433,630,425,930,64,266,235,187,284,665,874,80,45,848,38,811,267,575]
    print(A.InversePairs(L))