#!/usr/bin/python3
import os,sys,stat
#假定 /tmp/foo.txt 文件存在.
#设置所有者ID 为100
os.chown("/tmp/foo.txt",100,-1)

print("修改权限成功!!")

