#!/usr/bin/python3
import os,sys
#打开文件
fd=os.open("foo.txt",os.O_RDWR|os.O_CREAT)

#写入字符串
os.write(fd,str.encode("This is test"))

#关闭文件
os.close(fd)

print("关闭文件成功！！")

