#!/usr/bin/env python3
# -*- coding:utf-8 -*-

a=['zhangsan','lisi','wanglaowu']
print(a)
b=len(a)
print(b)
print(a[0])
print(a[-1])
a.append('laoliu')
print(a)
a.insert(0,'李二')
print(a)
a.pop()
print(a)
a.pop(0)
print(a)
a[0]='张三'
print(a)
b=["lier",a,"laolie"]
print(b)
print(b[1][1])


#元组
a=('zhangsan',1,True)
print(a[0])

t = ('a', 'b', ['A', 'B'])
print(t)
t[2][0]='x'
t[2][1]='y'
print(t)

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Bob']
]

# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Bob:
print(L[2][2])