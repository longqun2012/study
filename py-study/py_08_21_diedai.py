#!/usr/bin/env python3
# -*- coding=utf-8 -*-
from collections.abc import Iterable
d={'a':1,'b':2,'c':3}
for value in d:
    print(d[value])
for value in 'asdf':
    print(value)
l=['a','s','d','c']
for i,j in enumerate(l):
    print(i,j)
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x,y)
def findMinAndMax(x):
    if isinstance(x, Iterable)==True and x!=[]:
        min=max=x[0]
        for i in x:
            if i<min:
                min=i
            if i>max:
                max=i
        return min,max
    else:
        return None,None
print(findMinAndMax([]))
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')