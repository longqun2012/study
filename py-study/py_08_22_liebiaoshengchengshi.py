#!/usr/bin/env python3
# -*- coding=utf-8 -*-
import os

l=[x*x for x in range(1,10)]
print(l)

l=[x*x for x in range(3,13) if x%3==0]
print(l)

k=[x*y for x in range(1,5) for y in range(6,10)]
print(k)

s=[x for x in os.listdir('.')]
print(s)

d={'x':'1','y':'2','z':'3'}
s=[xx+'='+yx for xx,yx in d.items()]
# s=[k + '=' + v for k, v in d.items()]
print(s)
print("s")
d={'x':1,'y':2,'z':'3'}
s=[xx+'='+yx if isinstance(yx,str) else xx+str(yx) for xx,yx in d.items()]
print(s)
s=[xx+'='+yx if isinstance((xx,yx),str) else xx+str(yx) for xx,yx in d.items()]
print(s)
s=[xx+'='+yx if isinstance(yx,str) else xx+"="+str(yx) for xx,yx in d.items()]


# s=[k + '=' + v for k, v in d.items()]
print(s)

L = ['Hello', 'World', 18, 'Apple', None]
l=[x.lower() for x in L if isinstance(x,str)]
print(l)
l=[x.lower() if isinstance(x,str) else x for x in L]
print(l)