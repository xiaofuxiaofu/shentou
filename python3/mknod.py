#!/usr/bin/python3
import os
import stat
filename='/tmp/tmpfile'
mode = 600|stat.S_IRUSR

#文件系统节点指定不同模式
os.mknod(filename,mode)
