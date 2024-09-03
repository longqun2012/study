#!/user/bin/env python3 
# -*- coding=utf8 -*-


class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count +=1


# 测试:
print(Student.count)
if Student.count != 0:
    
    print('测试失败!')
else:
    bart = Student('Bart')
    print(Student.count)
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        print(Student.count)
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')


class Student(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
s = Student()
s.score = 60
print(s.score)
class Student2(object):
    # 方法名称和实例变量均为birth:
    @property
    def birth(self):
        return self.birth
a=Student2

class Screen(object):
    def __init__(self):
        self._width=0
        self.height=0
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self,value):
        if not isinstance(value,int):
            raise TypeError('err')
        self._width=value

    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self,value):
        self._height=value

    @property
    def resolution(self):
        return self.height*self.width

# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')