#!/usr/bin/python3
import os, sys
#打开文件
fd=os.open("foo.txt",os.O_RDWR|os.O_CREAT)

#获取元组
info=os.fstatvfs(fd)
print("文件信息：",info)

#获取文件名最大长度
print("文件名最大长度：%d" % info.f_namemax)

#获取可用块数
print("可用块数：%d" % info.f_bfree)

#关闭文件
os.close(fd)
