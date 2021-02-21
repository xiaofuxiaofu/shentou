#!/usr/bin/python3

import os

src='/usr/bin/python'
dst='/tmp/python'

#创建软连接
os.symlink(src,dst)

print("软连接创建成功")
