#!/usr/bin/python  
# coding:utf-8   
import httplib2  
import urllib2  
import re #正则表达式模块  
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

ReadFile = open(r"num.txt","r")
lines = ReadFile.readlines()
num=0
for line in lines:
	line = line.strip('\r\n')
	key=unicode(line)
	#print "key: ",key ,type(key)  
	num = re.findall(r'(\w*[0-9]+)\w*',key) 
	#print "num: ",num ,type(num)
	#print "str(num): ", str(num) ,type(str(num))
	num_convert =''.join(num)
	if(num_convert):
		print "num_convert: ",num_convert,type(num_convert)
		#url2 = url2 = "http://kansha.cc/pingfeng.aspx?w_nameno="+num_convert+"&w_dfbiao=booksdf3&w_df="+str(100)
		#print url2 