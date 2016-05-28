#-*- coding: utf8 -*-
import sys
import xlrd
from pyExcelerator import *
reload(sys)
sys.setdefaultencoding('utf-8')

num =0
ReadFileTime = open(r"sniffText.txt","r")
ReadFileResult = open(r"sniffResultBefore.txt","r")
w= Workbook()
ws=w.add_sheet("SniffResult")

Resultlines = ReadFileResult.readlines()
Timelines = ReadFileTime.readlines()




num=0
for line1 in Timelines:
	line1 = line1.strip('\r\n') 
	key=unicode(line1)
	print key
	key1= str(key)
	if len(key1) == 0:
		break
	list1 = key1.split( ) 
	name = list1[2]
	time = list1[5]
	print  list1[0],unicode(name) ,unicode(time)
	ws.write(num,1,unicode(name)) 
	ws.write(num,2,unicode(time)) 
	num=num+1
	print
num1=0
for line2 in Resultlines:
	line2 = line2.strip('\r\n')
	key=unicode(line2)
	print key
	key1= str(key)	
	if len(key1) == 0:
		break
	list1 = key1.split( ) 
	name = list1[2]
	result = list1[5]
	print  list1[0],unicode(name) ,unicode(result)
	ws.write(num1,3,unicode(name)) 
	ws.write(num1,4,unicode(result)) 
	num1=num1+1
	print


w.save("1.xls")
ReadFileTime.close()	
ReadFileResult.close()