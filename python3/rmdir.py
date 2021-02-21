#!/usr/bin/python3
import os ,sys

#列出目录
print("目录为：%s" % os.listdir(os.getcwd()))

#删除路径
os.rmdir("mydir")

#列出重命名后的目录
print("目录为：%s" % os.listdir(os.getcwd()))
