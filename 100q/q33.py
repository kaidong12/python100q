#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
题目：按逗号分隔列表。

"""

print()
print("==============Answer 1==============")

L = [1, 2, 3, 4, 5]
s1 = ','.join(str(n) for n in L)
print(s1)


print(','.join([str(n) for n in L]))
