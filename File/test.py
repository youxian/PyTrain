#-*- coding:utf-8 -*-

import urllib2
import httplib2
import sys 
import json 
def get_file(position):
	f =  open(position,'r')
	try:
		all_the_text = f.read( )
	finally:
		f.close( )
	return all_the_text

def main(): 

	print "txt file"
	position = "D:\PyWorkSpace\File\cookie.txt"
	cookieResult = "D:\PyWorkSpace\File\cookieResult.txt"
	writefile = file(cookieResult,'w')

	filecontent = get_file(position)
	#print filecontent
	#print type(filecontent) <type 'str'>
	fjson = json.loads(filecontent)
	#print fjson[0]['domain']
	#print type(fjson) <type 'list'>
	i=0
	for item in fjson:
		#print "type(item):",type(item)  # <type 'dict'>
		i=i+1
		writefile.write(str(i)+'\n')  
		print i
		#print "item",item 
		for itemlist in item: 
			#print u" 参数名：", itemlist,u" 参数值：", item[itemlist] 
			#writefile.write(str(itemlist) +": "+ str(item[itemlist])+'\n')
        	#print "item[",itemlist,"]",item[itemlist]
        	#print "type(itemlist1):",type(itemlist) #<type 'unicode'>
        	
        	
		
			if (str(itemlist) =="name"): 
				writefile.write("<elementProp name="+''+str(item[itemlist])+'"'+" "+"elementType="+'"'+"Cookie"+'"'+" "+"testname="+'"'+str(item[itemlist])+'">'+'\n')
			# 	writefile.write('''<longProp name="Cookie.expires">0</longProp>'''+'\n')
			# 	writefile.write('''<boolProp name="Cookie.path_specified">true</boolProp>'''+'\n')
			# 	writefile.write('''<boolProp name="Cookie.domain_specified">true</boolProp>'''+'\n')
			# elif(str(itemlist1)=="value" or "domain" or "domain" or "path"):
			# 	writefile.write("<elementProp name="+'"Cookie.'+ str(itemlist1) +'">'+str(item[itemlist1])+"</stringProp>"+'\n')







if __name__=="__main__":
	main()