#!/usr/bin/python3
import os,sys
#列出目录
print("目录为：%s" % os.listdir(os.getcwd()))

#移除
os.removedirs("/test")

#列出移除后的目录
print("移除后目录为：" % os.listdir(os.getcwd()))


