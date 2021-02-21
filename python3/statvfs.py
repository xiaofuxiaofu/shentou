#!/usr/bin/python3
import os,sys
#显示"a1.py"文件的statvfs 信息
stinfo = os.statvfs('a1.py')

print(stinfo)


