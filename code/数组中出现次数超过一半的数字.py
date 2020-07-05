#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/14 10:09
# @Author : XXX
# @title ： 数组中出现次数超过一半的数字
# @Site : 
# @File : 数组中出现次数超过一半的数字.py
# @Software: PyCharm

class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if numbers == []:
            return 0
        length = len(numbers)
        set_numbers = list(set(numbers))
        for value in set_numbers:
            count = 0
            copy_numbers = numbers
            while value in copy_numbers:
                copy_numbers.remove(value)
                count += 1
            if count > length / 2:
                return value
        return 0


class Solution2:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if numbers == []:
            return 0

        copy_numbers = numbers
        copy_numbers = sorted(copy_numbers)
        index = int(len(copy_numbers) / 2)
        value = copy_numbers[index]
        count = 0
        while value in copy_numbers:
            count += 1
            copy_numbers.remove(value)
        if count > len(numbers) / 2:
            return value
        else:
            return 0


if __name__ == '__main__':
    # A = Solution()
    # print(A.MoreThanHalfNum_Solution([1, 2, 3, 2, 2, 2, 5, 4, 2]))
    B = Solution2()
    print(B.MoreThanHalfNum_Solution([1,2,3,2,4,2,5,2,3]))