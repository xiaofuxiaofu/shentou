#!/usr/bin/python3
import os,stat
path="/tmp/foo.txt"

#为文件设置标记，是的它不能被重命名和删除
flags=stat.SF_NOUNLINK
retval=os.chflags(path,flags)
print("返回值：%s" % retval)

