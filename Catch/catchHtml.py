#!/usr/bin/python  
# coding:utf-8   
import httplib2  
import urllib2  
import re #正则表达式模块  
import sys
import r
reload(sys) 
sys.setdefaultencoding('utf-8')

#获取指定url的网页内容  
def get_page(url,headers):
	http=httplib2.Http()  
	response,content=http.request(url,'GET',headers=headers)  
	#return content.decode('unicode-escape').encode('utf-8') 
	return content 


          
def main():
	cookie1 = "ASP.NET_SessionId=lnjcyj45l1pnpd3jh5d3ldrr; CNZZDATA5693722=cnzz_eid%3D1767958995-1457572688-%26ntime%3D1457572688; amtek=userid=youxian20"              
   	headers ={"cookie":cookie1}
	url = "http://kansha.cc/myzx.aspx "
	content = get_page(url,headers)  
	sys1= sys.getfilesystemencoding()
	#print "sys1:",sys1
	html1 = content.decode("utf8").encode("mbcs")
	#print html1


	ReadFile = open(r"xuanhuan.txt","r") 
	writeFile =  open(r"pingfen.txt","a")
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
			#print "num_convert: ",num_convert,type(num_convert)
			url2 ="http://kansha.cc/pingfeng.aspx?w_nameno="+num_convert+"&w_dfbiao=booksdf3&w_df="+str(100)
			#print url2 
			writeFile.write(url2)
			writeFile.write("\n")


	ReadFile.close()
	writeFile.close()
  
if __name__ == "__main__":  
    main()  
