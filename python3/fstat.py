#!/usr/bin/python3
import os, sys

#打开文件
fd=os.open("foo.txt",os.O_RDWR|os.O_CREAT)

#获取元组
info=os.fstat(fd)
print("文件信息：", info)

#获取文件uid
print ("文件 UID：%d" % info.st_uid)

#获取文件gid
print("文件 GID：%d" % info.st_gid)

#关闭文件
os.close(fd)
