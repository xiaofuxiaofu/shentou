#!/usr/bin/python3
import os, sys, stat
#打开文件"/tmp/foo.txt"
fd=os.open("/tmp",os.O_RDONLY)

#设置文件可通过组执行
os.fchmod(fd,stat.S_IXGRP)

#设置文件可被其他用户写入
os.fchmod(fd,stat.S_IWOTH)

print("修改权限成功！！")

#关闭文件
os.close(fd)
