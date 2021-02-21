#!/usr/bin/python3
import os,sys
#显示当前目录
print("当前目录：%s" % os.getcwd())

#修改目录到/dev/tty
fd=os.open("/dev/tty",os.O_RDONLY)
f=os.tcgetpgrp(fd)

#显示进程组
print("相关进程组：")
print(f)

os.close(fd)
print("关闭文件成功！！")

