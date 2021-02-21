#!/usr/bin/python3
import os,sys
#打开文件
fd = os.open("f1.txt",os.O_RDWR)

#读取文件
ret=os.read(fd,12)
print (ret)

#关闭文件
os.close(fd)
print("关闭文件成功！！")
