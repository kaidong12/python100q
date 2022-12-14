#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
题目：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。

"""

print()
print("==============Answer 1==============")


def output(s, l):
    if l == 0:
        return
    print(s[l - 1])
    output(s, l - 1)


s = input('Input a string:')
l = len(s)
output(s, l)

print()
print("==============Answer 2==============")

def desc_output(s):
    if(len(s) > 0):
        print(s[-1])            # python 负数下标
        desc_output(s[0:-1])

s = input('Input a string:')
desc_output(s)

