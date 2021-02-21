#!/usr/bin/python3
import os ,sys
fd=os.open("foo.txt",os.O_RDWR|os.O_CREAT)
print("%s" % os.pathconf_names)
