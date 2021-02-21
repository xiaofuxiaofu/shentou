#!/usr/bin/python3
num = 1
def fun1():
    global num #需要使用global关键字声明
    print(num)
    num = 123
    print(num)
fun1()
print(num)
