#-*- coding:utf-8 -*-

try:
	f=open("1.txt",'r')
except IOError, e:
	print "could not find the file"