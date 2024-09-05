#!/usr/bin/env python3
# -*- coding=utf-8 -*- 

#对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，
# chr()函数把编码转换为对应的字符
ord('中')
a= '中午吃了没'
b=[]

print(b)
#将字符串a转换一个数字list
for x in a:
    c=ord(x)
    print('c=%d' %c)
    b.append(c)
    print(ord(x))
print(b)
#将一个数字list转换成字符串
c=''
for y in b:
    j=chr(y)
    c=c+j
print(c)

#encode ,decode
print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))
print(b'ABC'.decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

#len函数
print(len('asd'))

#占位符 	替换内容
# %d 	整数
# %f 	浮点数
# %s 	字符串
# %x 	十六进制整数
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)

print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))

r = 2.5
s = 3.14 * r ** 2
print(f'The area of a circle with radius {r} is {s:.2f}')

#练习
s1 = 72
s2 = 85
r =(s2-s1)*100/s1
print(f'{r:.1f}')