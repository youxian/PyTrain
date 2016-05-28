#!/usr/bin/python  
# coding:utf-8   
import httplib2  
import urllib2  
import re #正则表达式模块  
import sys
import time


reload(sys)
sys.setdefaultencoding('utf-8')

#获取指定url的网页内容  
def get_page(url,headers):
	http=httplib2.Http()  
	response,content=http.request(url,'GET',headers=headers)  
	#return content.decode('unicode-escape').encode('utf-8') 
	#return content


          
def main():

	ReadFile = open(r"test.txt","r")  
	lines = ReadFile.readlines()
	num=0
	for line in lines:
		num=num+1
		time.sleep(10)
		line = line.strip('\r\n')
		url2=unicode(line)
		print num, "url2: ",url2 ,type(url2)  
		cookie1 = "ASP.NET_SessionId=lnjcyj45l1pnpd3jh5d3ldrr; CNZZDATA5693722=cnzz_eid%3D1767958995-1457572688-%26ntime%3D1457572688; amtek=userid=youxian20"              
		headers ={"cookie":cookie1}
		content = get_page(url2,headers)  
		sys1= sys.getfilesystemencoding()
		print "sys1:",sys1
		#html1 = content.decode("utf8").encode("mbcs")
		#print html1
	
  
if __name__ == "__main__":  
    main()  
