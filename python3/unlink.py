#!/usr/bin/python3
import os,sys
#列出目录
print("目录为：%s" % os.listdir(os.getcwd()))

os.unlink("12.txt")

#删除后的目录
print("删除后的目录为：%s" % os.listdir(os.getcwd()))


