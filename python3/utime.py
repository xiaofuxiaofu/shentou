#!/usr/bin/python3
#-*- coding:UTF-8 -*-
import os,sys
#显示文件的stat信息
stinfo = os.stat('a2.py')
print(stinfo)

#使用os.stat来接收文件的访问和修改时间
print("a2.py的访问时间：%s" % stinfo.st_atime)
print("a2.py的修改时间：%s" % stinfo.st_mtime)

#修改访问和修改时间
os.utime("a2.py",(1330712280,1330712392))
print("done!!")
