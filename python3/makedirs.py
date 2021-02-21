#!/usr/bin/python3
import os ,sys
#创建的目录
path = "/tmp/home/monthly/daily"

os.makedirs(path,0o777);
print ("路径被创建")
