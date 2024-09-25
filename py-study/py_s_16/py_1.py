#!/usr/bin/env python3
# -*- coding=utf-8 -*-
import re
from datetime import datetime,timedelta,timezone
now=datetime.now()
print(now,type(now))

dt=datetime(2015,5,5,12,23,23)
print(dt)
#timestamp时间戳
print(now.timestamp())
t=1727167565.215631
print(datetime.fromtimestamp(t))
print(datetime.utcfromtimestamp(t))
print(datetime.fromtimestamp(timestamp=t))


strda=datetime.strptime('2012 2 2 16 22 22','%Y %m %d %H %M %S')
#年 Y 月m 天d 小时H 分钟M 秒S
print(strda)
print(strda.strftime('%m %d %H %S'))
strnow=datetime.now()
print(strnow)
if strnow>dt:
    print('超时')

print(strnow+timedelta(days=10))

tz_utf8=timezone(timedelta(hours=9))
print(tz_utf8)
a=now.replace(tzinfo=tz_utf8)

tz_utf10=timezone(timedelta(hours=10))
print(tz_utf10)
b=now.replace(tzinfo=tz_utf10)
print(a,'\n',b)
if a<b:
    print('jj')
else:
    print('uu')

sss=re.match(r'^\d{3}\-\d{3,8}$', '010-12345')
print(sss)
sss=re.match(r'^UTC\d{1,2}\d{2}$', 'UTC700')
print(sss)
def to_timestamp(dt_str, tz_str):
    dt_str_d=datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')
    #sm=re.match('^UTC[+|-][0-9]{1-2}\:[0-9]{1-2}$',tz_str)
    sm=re.match(r'^UTC\w{1}\d{1,2}:\d{2}$',tz_str)
    sm=re.match(r'^UTC([\+|\-])(\d{1,2}):(\d{2})$',tz_str)
    print(sm)
    print(sm.groups())
    dt=dt_str_d.replace(tzinfo=timezone(timedelta(hours=int(sm.group(2)) if sm.group(1)=='+' else -int(sm.group(2)))))
    print(dt.timestamp())
    return dt.timestamp()
# 测试:
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')