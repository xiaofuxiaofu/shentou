#!/usr/bin/python3
import os,sys
#打开文件
fd=os.open("foo.txt",os.O_RDWR|os.O_CREAT)
#写入字符串
str="this is test"
str=str.encode()
os.write(fd,str)

#关闭文件
os.closerange(fd,fd)
print("关闭文件成功!!")
