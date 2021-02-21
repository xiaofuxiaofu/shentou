#!/usr/bin/python3
import os
src='/usr/bin/python'
dst='/tmp/python'

#创建软连接
os.symlink(src,dst)

#使用软连接显示源链接
path=os.readlink(dst)
print(path)

