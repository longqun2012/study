#!/usr/bin/env python3
# -*- python -*-
L=[1,2,3,4,5,6,7,8,9]
print(L[0:3])
print(L[1:3])
print(L[-4:])
print(L[-4:-1])
print(L[-4:-2])
print(L[-1])
print(L[1])
print(L[:8:2])
print(L[::3])
print(L[:])

# def trim(a):
#     # le=len(a)
#     # i=0
#     # while i<le:
#     if a=='':
#         return a
#     elif a[0]==' ':
#         s=a[1:]
#         return trim(s)
#     elif a[-1]==' ':
#         s=a[:-1]
#         return trim(s)
#     else:
#         return a
#     # return a[i]

def trim(source):
    if not isinstance(source, str):
        raise TypeError("str must be a string")
    
    start = 0
    end = len(source)
    for chr in source:
        if chr == " ":
            start += 1
        else:
            break
    for chr in source[::-1]:
        if chr == " ":
            end -= 1
        else:
            break
    return source[start:end]

print(trim('   asdfsdsf   '))

if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')


print(trim('    '))