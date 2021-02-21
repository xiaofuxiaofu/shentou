#!/usr/bin/python3
import os,sys
#显示当前目录
print("当前目录：%s" % os.getcwd())

#修改目录为/dev/tty
fd=os.open("/dev/tty",os.O_RDONLY)
p=os.ttyname(fd)
print("关联的终端为：")
print(p)
print("done!!")
os.close(fd)

print("关闭文件成功！！")


