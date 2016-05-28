#-*- coding: UTF-8 -*-
#!/usr/bin/python

import time
import datetime

time1 = time.time()
print "time1: ",time1

start_sniff_time=datetime.datetime.now()
print "start_sniff_time:" ,start_sniff_time
#要度量时间的程序

OnlyNum("2001dsdklajdal121323")
i=1
while (i<10000000):
	i=1+i

time2 = time.time()
print "time2:",time2
print "time2-time1:",time2-time1


end_sniff_time=datetime.datetime.now()
print "end_sniff_time:" ,end_sniff_time
sniff_time = (end_sniff_time - start_sniff_time)
print "sniff_time: ",sniff_time