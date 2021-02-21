#!/usr/bin/python3
import os, sys, stat

#打开文件"/tmp/foo.txt"
fd=os.open("/tmp",os.O_RDONLY)

#设置文件的用户id为100
os.fchown(fd,100,-1)

#设置文件的用户组id为50
os.fchown(fd,-1,50)

print("修改权限成功！！")

#关闭文件
os.close(fd)
