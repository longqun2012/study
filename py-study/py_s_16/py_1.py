#!/usr/bin/env python3
# -*- coding=utf-8 -*-

from datetime import datetime
now=datetime.now()
print(now,type(now))

dt=datetime(2015,5,5,12,23,23)
print(dt)
print(now.timestamp())
t=1727167565.215631
print(datetime.fromtimestamp(t))
print(datetime.utcfromtimestamp(t))
print(datetime.fromtimestamp(timestamp=t))