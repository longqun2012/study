#!/usr/bin/env python3
# -*- coding=utf-8 -*-

class mini():
    def __init__(self) -> None:
        pass
    def run(self):
        print('mini run')
class mini_a(mini):
    def __init__(self) -> None:
        pass
    def run(self):
        print('mini_a run')
class mini_b(mini):
    def __init__(self) -> None:
        super().__init__()
    def run(self):
        print('mini_b run')
class mini_d(mini):
    def __init__(self) -> None:
        super().__init__()
a=mini()
a.run()
print(isinstance(a,mini))
print(isinstance(a,mini_a))
b=mini_a()
print(isinstance(b,mini))
print(isinstance(b,mini_a))
b.run()
c=mini_b()
c.run()
d=mini_d()
d.run()
print('#')
def two_pri(mini):
    mini.run()
    mini.run()
two_pri(mini())
two_pri(mini_a())