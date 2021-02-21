#!/usr/bin/python3
import os ,sys
#创建的目录
path = "/tmp/hourly"

os.mkfifo(path,644)
print("路径被创建")
