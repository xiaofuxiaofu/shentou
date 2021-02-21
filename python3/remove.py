#!/usr/bin/python3
import os, sys
#列出目录
print("目录为：%s" % os.listdir(os.getcwd()))

#移除
os.remove("txt")

#移除后列出目录
print("移除后：%s" % os.listdir(os.getcwd()))

