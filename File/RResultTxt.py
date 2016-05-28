#-*- coding: utf8 -*-
import sys


reload(sys)
sys.setdefaultencoding('utf-8')

ReadFile = open(r"sniffResultBefore.txt","r")
lines = ReadFile.readlines()
num=0
for line in lines:
	line = line.strip('\r\n')
	key=unicode(line)
	print key
	key1= str(key)
	list1 = key1.split( ) 
	name = list1[2]
	time = list1[5]
	print  list1[0],unicode(name) ,unicode(time)
	print