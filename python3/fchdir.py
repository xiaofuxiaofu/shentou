#!/usr/bin/python3
import os, sys
#首先目录 "/var/www/html"
os.chdir("/var/www/html")

#输出当前目录
print ("当前工作目录为：%s" % os.getcwd())

#打开新目录"/tmp"
fd=os.open("/tmp",os.O_RDONLY)

#使用os.fchdir()方法修改到新目录
os.fchdir(fd)

#输出当前目录
print ("当前工作目录为：%s" % os.getcwd())

#关闭打开的目录
os.close(fd)

