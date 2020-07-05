#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/14 18:43
# @Author : XXX
# @title ： 把数组排成最小的数
# @Site : 
# @File : 把数组排成最小的数.py
# @Software: PyCharm


class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if len(numbers) == 1:
            return numbers[0]

        copy_numbers = []
        for value in numbers:
            if copy_numbers == []:
                copy_numbers.append(value)
            else:
                index = []
                for i in range(len(copy_numbers)):
                    if self.Compare_str(value, copy_numbers[i]):
                        index.append(i)
                    else:
                        index.append(i+1)
                if 0 in index:
                    copy_numbers.insert(0,value)
                elif len(copy_numbers) in index:
                    copy_numbers.insert(len(copy_numbers),value)
                else:
                    index_set = list(set(index))
                    for set_num in index_set:
                        if index.count(set_num) == 2:
                            copy_numbers.insert(set_num, value)
        return "".join(map(str,copy_numbers))

    def Compare_str(self, num1, num2):
        str1 = str(num1)
        str2 = str(num2)
        if int(str1 + str2) >= int(str2 + str1):
            return False
        else:
            return True


if __name__ == '__main__':
    A = Solution()
    print(A.PrintMinNumber([3,5,1,4,2]))
    # a = [3, 5, 1, 4, 2]
    # a.insert(1,8)
    # print(a)

