#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import re
addr='asd@asd.com'
if re.match(r'^[a-z][a-z\.]*@[a-z]*\.com$',addr)==None:
    print('2')
else:
    print('1')
def is_valid_email(addr):
    a=re.match(r'^[a-zA-Z][a-zA-Z0-9\.]*@[a-zA-Z0-9\.]*\.com$',addr)
    print(a)
    if a==None:
        return False
    else:
        return True

# 测试:
assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')