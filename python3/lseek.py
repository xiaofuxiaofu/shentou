#/usr/bin/python3
import os,sys
#打开文件
fd=os.open("foo.txt",os.O_RDWR|os.O_CREAT)
a="This is test"
#写入字符串
os.write(fd,bytes(a,'UTF-8'))

#从开始位置读取字符串
os.lseek(fd,0,0)
str=os.read(fd,100)
print("Read String is :",str)

#关闭文件
os.close(fd)

print("关闭文件成功！！")
