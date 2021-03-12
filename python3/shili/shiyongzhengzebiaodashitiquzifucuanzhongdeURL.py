#!/usr/bin/python3
import re

def Find(string):
    # findall() 查找皮喷正则表达式的字符串,调用时死记硬背。
    url = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+',string)
    return url

string = 'Runoob 的网页地址为：https://www.runoob.com, Google 的网页地址为:https://www.goole.com'
print("Urls:",Find(string))

