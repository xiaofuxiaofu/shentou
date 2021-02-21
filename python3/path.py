#!/usr/bin/python3
import os

#返回文件名
print(os.path.basename('/root/runoob.txt'))

#返回目录路径
print(os.path.dirname('/root/runoob.txt'))

#分割文件名与路径
print(os.path.split('/root/ruoob.txt'))

#将目录和文件名合成一个路径
print(os.path.join('root','test','runoob.txt'))

