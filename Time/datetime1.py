#-*- coding:utf-8 -*-
import datetime
import time
def runtime():
	i=1
	j=1
	while i<100000000:	
		while  j<100000000000:
			i=i+j
			j=i+j
#1.序开始到程序结束的运行时间
starttime1 = datetime.datetime.now()
runtime()
endtime1 = datetime.datetime.now()
print "seconds:",(endtime1 - starttime1).seconds
print "microseconds:",(endtime1 - starttime1).microseconds

#2.程序开始到程序结束的运行时间
starttime2 = time.time()
runtime()
endtime2 = time.time
# time1= (endtime2-starttime2).seconds
# print time1


#3.只计算了程序运行的CPU时间
starttime3 = time.clock()
runtime()
endtime3 = time.clock()
print endtime3- starttime3
