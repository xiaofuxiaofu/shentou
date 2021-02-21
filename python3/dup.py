#!/usr/bin/python3
import os ,sys
#打开文件
fd=os.open("foo.txt", os.O_RDWR|os.O_CREAT)

#复制文件描述符
d_fd = os.dup(fd)

#使用复制的文件描述符写入文件
os.write(d_fd,"This is test".encode())

#关闭文件
os.closerange(fd,d_fd)

print("关闭所有文件成功!!!")
