#!/usr/bin/python3
import os,sys
#打开文件
path="/var/www/html/foo.txt"
fd=os.open(path,os.O_RDWR|os.O_CREAT)

#关闭文件
os.close(fd)

#创建以上文件的拷贝
dst="/tmp/foo.txt"
os.link(path,dst)

print("创建硬链接成功！！")
