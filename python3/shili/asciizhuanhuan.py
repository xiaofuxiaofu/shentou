#!/usr/bin/python3
#用户输入符
c =input("请输入一个字符：")
#用户输入ACSII码，并将输入的数字转为整形
a = int(input("请输入一个ASCII码："))

print(c + " 的ASCII码为", ord(c))
print(a , " 对应的字符为", chr(a))
