#!/usr/bin/python3
import os ,sys
#打开文件
fd=os.open("foo.txt",os.O_RDWR|os.O_CREAT)

#写入字符串
str="This is runoob.com site"
os.write(fd,bytes(str,'UTF-8'))

#使用isatty(fd)
ret=os.isatty(fd)
print("返回值：",ret)

#关闭文件
os.close(fd)


