#!/usr/bin/python3
def check(string,sub_str):
    if (string.find(sub_str) == -1):          #如果不包含索引值，返回-1
        print("不存在！")
    else:
        print("存在！")
string = "www.runoob.com"
sub_str = "runoob"
check(string,sub_str)


