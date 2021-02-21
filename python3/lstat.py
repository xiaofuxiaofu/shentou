#!/usr/bin/python3
import os,sys
#打开文件
path="/var/www/html/foo.txt"
fd=os.open(path,os.O_RDWR|os.O_CREAT)
#关闭打开的文件
os.close(fd)

#获取元组
info=os.lstat(path)
print("文件信息：",info)

#获取文件 uid
print ("文件UID：%d" % info.st_uid)

#获取文件 gid
print ("文件 GID：%d" % info.st_gid)
