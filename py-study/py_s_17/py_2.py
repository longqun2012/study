#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import requests
# r=requests.get('https://www.douban.com/')
r = requests.get('https://www.douban.com/', headers={'User-Agent': 'M'})
#r = requests.get('https://www.baidu.com')
print(r.status_code)
print(r.text)
r = requests.get('https://www.douban.com/', headers={'User-Agent': 'M'}, params={'q':'python3','cat':'1001'})
print(r.url)
print(r.encoding)

print(r.content)
print(r.headers)
print(r.headers['Content-type'])
print(r.cookies)
print(r.cookies['ll'])
#json格式
#print(r.json())

#post
r=requests.post(url='https://www.douban.com/login/',data={'email':'aaa@163.com','password':'aaa',})
par={'key':'value'}
r=requests.post(url='https://www.douban.com/login/',json=par)

# 要在请求中传入Cookie，只需准备一个dict传入cookies参数：

# >>> cs = {'token': '12345', 'status': 'working'}
# >>> r = requests.get(url, cookies=cs)

# 最后，要指定超时，传入以秒为单位的timeout参数：

# >>> r = requests.get(url, timeout=2.5) # 2.5秒后超时
