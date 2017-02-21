#!/usr/bin/python
import time;

localtime = time.localtime(time.time())
print localtime
print "---------------------------------"
print str(localtime.tm_year)+"-"+str(localtime.tm_mon)+"-"+str(localtime.tm_mday)