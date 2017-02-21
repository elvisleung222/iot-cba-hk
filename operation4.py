#!/usr/bin/python
import time;

localtime = time.localtime(time.time())
print localtime
print "---------------------------------"
print localtime.tm_year+"-"+localtime.tm_mon+"-"+localtime.tm_mday