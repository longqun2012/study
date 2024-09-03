#!/usr/bin/env python3
# -*- coding=utf-8 -*-

class ren(object):
    rensu=0
    def __init__(self):
        self.__shengao=None
        self.__tizhong=None
        ren.rensu+=1
    __slots__=('name','age','__shengao','__tizhong')
    def typecheck(self,value):
        if not isinstance(value,(int,float)):
            raise "typeerr"

    @property
    def shengao(self):
        return self.__shengao
    @shengao.setter
    def shengao(self,value):
        self.typecheck(value)
        self.__shengao=value
    
    @property
    def tizhong(self):
        return self.__tizhong
    @tizhong.setter
    def tizhong(self,value):
        self.typecheck(value)
        self.__tizhong=value
    
    @property
    def wei(self):
        return self.__tizhong/self.__shengao

class ch(ren):
    __slots__=('__dizhi','__area','loca','yuyan')
    def __init__(self):
        super().__init__()
        self.loca=None
        self.__dizhi=None
    # def get_ared(self):
    #     return self.__area
    def set_dizhi(self,value):
        self.__dizhi=value
    def get_dizhi(self):
        return self.__dizhi
    def get_area(self):
        match self.__dizhi:
            case None:
                return '无地域'
            case '河南'|'河北':
                return '北方人'
            case "吉林"|"黑龙江":
                return '东北人'
            case _:
                return '南方人'


#
def sus(self,age):
    self.age=age
ren.sus=sus

# 测试:
s = ren()
s.shengao = 1.7
s.tizhong = 55
print(s.shengao)
print('resolution =', s.wei)

s.sus(11)
print(s.age)

if s.wei == 786432:
    print('测试通过!')
else:
    print('测试失败!')
print(ren.rensu)


nanfangren=ch()
print('子类创建后',ren.rensu)
nanfangren.get_area()
print(nanfangren.get_area())
nanfangren.set_dizhi('河南')
print(nanfangren.get_area())
nanfangren.set_dizhi('黑龙江')
print(nanfangren.get_area())
nanfangren.set_dizhi('shanghai')
print(nanfangren.get_area())

nanfangren.shengao=1.65
nanfangren.tizhong=50
print(nanfangren.wei)
print(dir(nanfangren))

print(hasattr(nanfangren,'dizhi'))
print(hasattr(nanfangren,'__dizhi'))
print(hasattr(nanfangren,'loca'))
print(nanfangren.loca)
setattr(nanfangren,'yuyan','naning')
print(hasattr(nanfangren,'yuyan'))
print(nanfangren.yuyan)
print(getattr(nanfangren,'yuyan'))
print(getattr(nanfangren,'yuyan1','404 not found'))

a=getattr(nanfangren,'get_area')
print(a())
print(ren.rensu)