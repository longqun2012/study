#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#coding=utf-8
a=ord('中')
print(a)
a=ord('a')
print(a)
b=chr(88)
print(b)
c='\u4e2d\u6587'
print(c)
print('\u4e2d\u6587')
x = b'ABC'
print(x)
a="中文".encode('utf-8')
print(a)
b=b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
print(b)
a="a".encode('ascii')
print(a)
b=b'a'.decode('utf-8')
print(b)
x=len("asdf")
print(x)
print("hi,%s.你今年%d岁" %("longqun",27))
print('%2d-%03d' % (3, 1))
print('%.2f' % 3.1415926)

print("hi,%s,你今年%s岁,成绩提升了%s%%"%('longqun',27,4))

print('hi,{0},你今年{1:.1f}岁'.format('longqun',17.111))
a=3
s=3.1415926*a**2
print(f'半径是{a}圆的面积是{s:.2f}')
s1=72
s2=85
a=(s2-s1)*100/s1
print(f'小明的成绩提升率是{a:.1f}%')