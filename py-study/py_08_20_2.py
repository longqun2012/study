#!/usr/bin/env python3
# -*- coding:utf-8 -*-

a=input("请输入身高")
b=input("请输入体重")
print(a,b)
x=float(a)
y=float(b)
MBI=y/x**2
if MBI<18.5:
    print("过轻")
elif MBI<25:
    print("正常")
elif MBI<28:
    print("过重")
elif MBI<32:
    print("肥胖")
else:
    print("过度肥胖")