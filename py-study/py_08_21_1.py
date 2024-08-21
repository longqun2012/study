#!/usr/bin/env python3
# -*- coding=utf-8 -*-
import py_08_21_function

a=hex(255)
b=hex(100)
print(f'{a}\n{b}')

x=py_08_21_function.my_abs(-1)
print(x)

# x=py_08_21_function.my_abs("a")
# print(x)

x,y=py_08_21_function.my_yd(100,200,300,60)
print(x,y)

x=py_08_21_function.my_qua(1,'a',1)
print(x)
print(py_08_21_function.my_qua(2, 3, 1))
if py_08_21_function.my_qua(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif py_08_21_function.my_qua(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')

print(py_08_21_function.my_power(6,3))
print(py_08_21_function.my_power(6))

print(py_08_21_function.my_calc(1,2,2))

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
d['Bob']={77:88}
print(d['Bob'][77])

print(py_08_21_function.my_person("long",27,city='shanghai',stu='xtu'))

xxon={'city':'shanghai','stu':'xtu'}
print(py_08_21_function.my_person("long",27,**xxon))
py_08_21_function.my_person("long",27,**xxon)

x=(1,2,4)
print(py_08_21_function.mul(*x))
# print(py_08_21_function.mul())