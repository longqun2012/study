#!/usr/bin/env python3
# -*- coding=utf-8 -*-

a=list(filter(lambda x: x%2==1,range(1,20)))
print(a)


#装饰器

import time, functools

def metric(fn):
    @functools.wraps(fn)
    def wap(*args,**KW):
        print('%s executed in %s ms' % (fn.__name__, 10.24))
        return fn(*args,**KW)
    return wap

# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
else:
    print("成功")

def log(asds=None):
    if callable(asds):
        return log()(asds)
    def metric(fn):
        @functools.wraps(fn)
        def wap(*args,**KW):
            print('%s : %s executed in %s ms' % (asds,fn.__name__, 10.24))
            return fn(*args,**KW)
        return wap
    return metric
# def log(text=None):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args,**kw):
#             print('begin call')
#             if callable(text): # 此时text是函数，说明装饰器没有参数
#                 print('call %s():' % func.__name__)
#             else: # 此时text是文本，说明装饰器含有参数
#                 print('%s %s():' % (text,func.__name__))
#             print(func(*args,**kw))
#             print('end call')
#             return func(*args,**kw)
#         return wrapper
#     if callable(text): # 此时text是函数，说明装饰器没有参数
#         return decorator(text)
#     return decorator  # 此时text是文本，说明装饰器含有参数

@log('execute')
def f():
    pass

@log
def fs():
    pass
a=f()
a=fs()