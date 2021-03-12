#!/usr/bin/python3
def findLen(str):
    counter = 0
    while str[counter:]:
        counter +=1
    return counter

str = "runoob"
print(findLen(str))
