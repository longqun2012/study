#!/usr/bin/env python3
# -*- python -*-
import math
def my_type_s(a):
    if not isinstance(a,(int,float)):
        raise 'typeerror'
    else:
        pass

def my_abs(a):
    if not isinstance(a,(int,float)):
        raise 'typeerror'
    if a>=0:
        return a
    else:
        return -a
    
def my_yd(x,y,z,angle=0):
    nx=x+z*math.cos(angle)
    ny=y+z*math.sin(angle)
    return nx,ny

def my_qua(a,b,c):
    if not all(isinstance(i,(int,float))for i in (a,b,c)):
        raise TypeError('bad operand type test')
    my_type_s(a)
    my_type_s(b)
    my_type_s(c)
    if a==0:
        if b==0:
            return "这不是方程"
        else:
            x=-c/b
            return x
    elif b**2-4*a*c<0:
        return "此方程无解"
    elif b**2-4*a*c==0:
        x=-b/(2*a)
        return x
    else:
        x=(-b+math.sqrt(b**2-4*a*c))/(2*a)
        y=(-b-math.sqrt(b**2-4*a*c))/(2*a)
        return x,y
    
def my_power(x,y=2):
    s=1
    while y>0:
        s=s*x
        y=y-1
    return s

def my_a_add(L=[]):
    L.append('end')
    return L
# print(my_a_add())
# print(my_a_add())

def my_a_add2(L=None):
    if L == None:
        L=[]
    L.append('end')
    return L
# print(my_a_add2())
# print(my_a_add2())

# a=my_abs(-2)
# print(a)

# x=math.sin(math.pi/6)
# print(x)

def my_calc(*number):
    s=0
    for i in number:
        s=s+i**2
    return s

def my_person(name,age,**other):
    print("name:",name,"age:",age,"other:",other)
    # pass

def mul(*x):
    if x==():
        raise "typeerror"
    elif not all(isinstance(i,(int,float))for i in x):
        raise TypeError
    else:
        s=1
        for i in x:
            s=s*i
        return s

def my_fex(n):
    if n==1:
        return 1
    else:
        return n*my_fex(n-1)
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)
print(fact(5))
print(my_fex(100))
# if mul(5) != 5:
#     print('mul(5)测试失败!')
# elif mul(5, 6) != 30:
#     print('mul(5, 6)测试失败!')
# elif mul(5, 6, 7) != 210:
#     print('mul(5, 6, 7)测试失败!')
# elif mul(5, 6, 7, 9) != 1890:
#     print('mul(5, 6, 7, 9)测试失败!')
# else:
#     try:
#         mul()
#         print('mul()测试失败!')
#     except TypeError:
#         print('测试成功!')


def fac(n):
    return fex(n,1)
def fex(x,y):
    if x==1:
        return y
    return fex(x-1,x*y)
# print(fac(1000))


def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
# print(fact(1000))

def move(n,a,b,c):
    if n==1:
        print(a,"==>",c)
    else:
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)

move(3,"a","b","c")