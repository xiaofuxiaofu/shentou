#!/usr/bin/python3
import os,sys
#打开文件
path="/var/www/html/foo.txt"
fd=os.open(path,os.O_RDWR|os.O_CREAT)

#关闭文件
os.close(fd)

#修改文件标记
ret=os.lchflags(path,os.UF_IMMUTABLE)
print("修改文件标记成功！！")
