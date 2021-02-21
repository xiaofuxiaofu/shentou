#!/usr/bin/python3
import os
#主 pty,从tty
m,s = os.openpty()

print(m)
print(s)

#显示终端名
s=os.ttyname(s)
print(m)
print(s)
