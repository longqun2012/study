#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import psutil
import psutil.tests
print(psutil.cpu_count())#cpu逻辑核心数量


print(psutil.cpu_count(logical=False))#cpu物理核心数量

print(psutil.cpu_times())#统计CPU的用户／系统／空闲时间

#cpu使用率
# for x in range(10):
#     print(psutil.cpu_percent(interval=1,percpu=True))

#查看内存
#查看交换内存
print(psutil.swap_memory())
#查看物理内存
print(psutil.virtual_memory())


#查看磁盘
#磁盘分区
print(psutil.disk_partitions())
#磁盘io
print(psutil.disk_io_counters())
#磁盘使用情况
print(psutil.disk_usage('/'))

#查看网络
print(psutil.net_io_counters())

print(psutil.net_if_addrs())

print(psutil.net_if_stats())

# 查看进程
#print(psutil.test()) # 等于ps

print(psutil.pids())
p=psutil.Process(3772)
print(p.name())
print(p.exe())
# print(p.cwd())
# print(p.cmdline())