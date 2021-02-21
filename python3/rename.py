#!/usr/bin/python3
import os,sys
#列出目录
print("目录为：%s" % os.listdir(os.getcwd()))

#重命名
os.rename("test","test2")

print ("重命名成功。")

#列出重命名后的目录
print("目录为：%s" % os.listdir(os.getcwd()))


