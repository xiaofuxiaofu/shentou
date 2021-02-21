#!/usr/bin/python3
import os
#当前工作目录
path=os.getcwd()
print("当前工作目录：",path)

#父目录
parent = os.path.join(path,os.pardir)

#父目录
#print("\n父目录：",os.path.abspath(parent))
print("\n父目录：",parent)
