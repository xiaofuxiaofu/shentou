#!/usr/bin/python3
import os ,sys
print ("当前目录为：%s" % os.getcwd())

#列出目录
print("目录为：%s" % os.listdir(os.getcwd()))

#重命名"aa1.txt"
os.renames("aa1.txt","newdir/aanew.txt")
print("重命名成功。")

#列出重命名的文件"aa1.txt"
print("目录为：%s" % os.listdir(os.getcwd()))


