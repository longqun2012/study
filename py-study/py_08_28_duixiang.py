#!/usr/bin/env python3 
# -*- coding=utf-8 -*-
class Student(object):
    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender
    def get_gender(self):
        return self.__gender
    def set_gender(self, gender):
        if gender=='':
            raise 'type error'
        elif isinstance(gender,str):
            self.__gender=gender
        else:
            raise 'ty'

# 测试:
bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('1')
    print('测试失败!')
else:
    bart.set_gender('female')
    print('2')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')
bart.set_gender('')
a=bart.get_gender()
print(a)