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
            print("I",i)
        return su
    return sum
f=xs(*a)
print(f)
print(f())
print(f())

def count():
    fs = []
    for i in range(1, 4):
        def f():
            print("I",i)
            return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())

def count2():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        print('i',i)
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs
f1, f2, f3 = count2()
print(f1())
# print(f2())
# print(f3())


# def createCounter():
#     i=0
#     def counter():
#         nonlocal i
#         while True:
            
#             i=i+1
#             yield i
#     def xs():
#         next(counter())
#     return xs
#     #return n
def createCounter():
    init = 0
    def counter():
        nonlocal init
        init = init + 1
        return init
    return counter
# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())
 # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')