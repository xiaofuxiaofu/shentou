#!/usr/bin/python3
import os,sys
#打开文件
path="/var/www/html/foo.txt"
fd=os.open(path,os.O_RDWR|os.O_CREAT)
#关闭打开的文件
os.close(fd)

#修改文件权限
#设置文件所属用户 ID
os.lchown(path,500,-1)

#设置文件所属用户组 ID
os.lchown(path,-1,500)
print("修改权限成功！！")
