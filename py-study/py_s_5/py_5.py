#!/usr/bin/env python3
# -*- coding=utf-8 -*- 
score=10
match score:
    case x if x<10:
        print('s')
    case 10|11:
        print('x')
    case 12:
        print('12')
    case _:
        print('oth')

arg=['a','b','c']
match arg:
    case ['a']:
        print('err')
    case ['a',file,*file1]:
        print('a'+file+','.join(file1))