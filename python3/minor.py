#!/usr/bin/python3
import os,sys
path="/var/www/html/foo.txt"

#获取元组
info=os.lstat(path)

#获取major 和minor 设备号
major_dnum = os.major(info.st_dev)
minor_dnum = os.minor(info.st_dev)

print("Major设备号：",major_dnum)
print("Minor设备号：",minor_dnum)


