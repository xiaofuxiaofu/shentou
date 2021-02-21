#!/usr/bin/python3
import os, sys
#打开文件
path="/var/www/html/foo.txt"
fd=os.open(path,os.O_RDWR|os.O_CREAT)

#关闭文件
os.close(fd)

#修改文件权限
#设置文件可以通过组执行
os.lchmod(path,stat.S_IXGRP)

#设置文件可以被其他用户写入
os.lchmod("/tmp/foo.txt",stat.S_IWOTH)
print("修改权限成功！！")

