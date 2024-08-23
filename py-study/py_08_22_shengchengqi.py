#!/usr/bin/env python3
# -*- coding=utf-8 -*-

g=(x*x for x in range(0,10))
print(next(g))
print(next(g))
print(next(g))
for n in g:
    print(n)

def fbo(max):
    x,a=0,0
    b=1
    while x<max:
        print(b)
        a,b=b,a+b
        x=x+1
    return "don"
fbo(6)
def fbi(max):
    x,a=0,0
    b=1
    while x<max:
        yield b
        a,b=b,a+b
        x=x+1
    return "don"

def odd():
    print('s 1')
    yield 1
    print('s 2')
    yield 2
    print('s 3')
    yield 4
o=odd()
next(o)
next(o)
next(o)
next(odd())
next(odd())
next(odd())
# next(o)
f=fbi(6)
print(f)
for n in fbi(6):
    print(n)

while True:
    try:
        a=next(f)
        print(a)
    except StopIteration as e:
        print('asd',e.value)
        break
l=[1]+[1]
print(l)
def triangles(max):
    a=0
    b=0
    d=[1]
    while a<max:
        yield d
        d=[1]+[d[a]+d[a+1] for a in range(len(d)-1)]+[1]
        a=a+1
        # while b<a:
        #     d=[1]+[1]
x=int(input())
a=triangles(x)
while True:
    try:
        b=next(a)
        print(b)
    except StopIteration as a:
        #print('asd',a.value)
        break

a=range(2)
print(a)
# # 期待输出:
# # [1]
# # [1, 1]
# # [1, 2, 1]
# # [1, 3, 3, 1]
# # [1, 4, 6, 4, 1]
# # [1, 5, 10, 10, 5, 1]
# # [1, 6, 15, 20, 15, 6, 1]
# # [1, 7, 21, 35, 35, 21, 7, 1]
# # [1, 8, 28, 56, 70, 56, 28, 8, 1]
# # [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
# n = 0
# results = []
# for t in triangles():
#     results.append(t)
#     n = n + 1
#     if n == 10:
#         break

# for t in results:
#     print(t)

# if results == [
#     [1],
#     [1, 1],
#     [1, 2, 1],
#     [1, 3, 3, 1],
#     [1, 4, 6, 4, 1],
#     [1, 5, 10, 10, 5, 1],
#     [1, 6, 15, 20, 15, 6, 1],
#     [1, 7, 21, 35, 35, 21, 7, 1],
#     [1, 8, 28, 56, 70, 56, 28, 8, 1],
#     [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
# ]:
#     print('测试通过!')
# else:
#     print('测试失败!')