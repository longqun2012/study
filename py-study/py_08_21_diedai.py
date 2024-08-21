#!/usr/bin/env python3
# -*- coding=utf-8 -*-
from collections.abc import Iterable

def findMinAndMax(x):
    if x and isinstance(x, Iterable)==True:
        min,max=x[0]
        for i in x:
            if i<min:
                min=i
            if i>max:
                max=i
        return min,max
    else:
        return None,None
print(findMinAndMax([7]))
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7,7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')