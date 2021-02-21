#!/usr/bin/python3
import os, sys
#打开文件
fd =os.open("foo.txt",os.O_RDWR|os.O_CREAT)

print("%s" % os.pathconf_names)

#获取最大文件连接数
no = os.fpathconf(fd,'PC_LINK_MAX')
print ("文件最大连接数为：%d" % no)

#获取文件名最大长度
no=os.fpathconf(fd,'PC_NAME_MAX')
print("文件名最大长度为：%d" % no)

#关闭文件
os.close(fd)

print("关闭文件成功！！")
