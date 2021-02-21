#!/usr/bin/python3
import os,sys
#Stat 信息
statinfo = os.stat('a2.py')
print (statinfo)
statinfo = os.stat_float_times()
print(statinfo)
