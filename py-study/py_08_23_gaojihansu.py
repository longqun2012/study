#!/usr/bin/env python3
# -*- coding=utf-8 -*-
def add(x, y, f):
    return f(x) + f(y)

print(add(-5, 6, abs))


#map
def cheng(x):
    return x*x
x=map(cheng,[x for x in range(1,10)])
print(list(x))
b=list(map(str,range(19)))
print(b)



#reduce
import functools
def jiafa(x,y):
    # print(x)
    # print(y)
    z=x*10+y
    return z
c=functools.reduce(jiafa,range(101))
print(c)

x="24567"
d={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
def strtoint2(x):
    def jia(x,y):
        return x*10+y
    def dia(x):
        return d[x]
    return x,functools.reduce(jia,map(dia,x))
print(strtoint2("24567"))

def normalize(name):
    x=name[0:1]
    y=name[1:]
    a=x.upper()
    b=y.lower()
    return a+b

# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

# s1='a'
# s2=s1[:1]
# print(s2)
# s6=s2.upper()
# s3=s1[1:]
# print(s3)
# s4=s3.lower()
# print(s4)
# s5=s6+s4
# print(s5)

def prod(L):
    def cheng(x,y):
        return x*y
    return functools.reduce(cheng,L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

def str2float(s):
    def de(x):
        return d[x]
    def xe(x):
        y=len(x)
        #i=0
        for i,j in enumerate(x):
            if j=='.':
                return y-i-1
    k=xe(s)
    print(k)
    l=s.replace('.','')
    print(l)
    ssy=functools.reduce(lambda x,y:x*10+y,map(de,l))/pow(10,k)
    print(ssy)
    return functools.reduce(lambda x,y:x*10+y,map(de,l))/pow(10,k)

    # def ce(x,y):
    #     return x*10+y
    # def ce2(x,y):
    #     return x+y/10
    #functools.reduce(ce,map(de,s))

print('str2float(\'123.456\') =', str2float('123.456'))
# if abs(str2float('123.456') - 123.456) < 0.00001:
#     print('测试成功!')
# else:
#     print('测试失败!')