#!/usr/bin/env python3
# -*- python -*-

def cansu(x,y=1,*sum,tag,**oth):
    print(f'x:{x},y:{y},sd:{sum},asd:{tag},{oth}')
cansu('a',1,2,3,4,tag=2,adu=3,ad=2)