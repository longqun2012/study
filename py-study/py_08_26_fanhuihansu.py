#!/use/bin/env python3
# -*- coding=utf-8 -*-

def inc():
    x = 0
    def fn():
        # nonlocal x
        #x = x + 1
        return x+1
    return fn

f = inc()
print(f()) # 1
print(f()) # 2

def sum(*arg):
    su=0
    for i in arg:
        su=su+i
    return su
a=[1,2,3]
print(sum(*a))

def xs(*arg):
    def sum():
        su=0
        for i in arg:
            su=su+i
            return su
    return sum
f=xs(*a)
print(f)
print(f())
print(f())
