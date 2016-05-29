#-*- coding:utf-8 -*-

import urllib2
import httplib2
import sys 
import json

def get_page(url):
	http = httplib2.Http()
	response, content = http.request(url,'GET')
	return content

def get_file(position):
	f =  open(position,'r')
	try:
		all_the_text = f.read( )
	finally:
		f.close( )
	return all_the_text

def main(): 

	print "url  json"
	url="http://home.m.sjzhushou.com/homepage/refreshpage?device=iPhone8%2C1&id=37458505856513&ios_ver=9.3.1&length=8&mobile_type=iOS&partnerId=0x20800003&peerID=6e0429b792be003V&peer_id=6e0429b792be003V&productID=31&product_id=31&ts=1463477985&ver=5.18.1.3079&versionCode=51801"
	urlcontent = get_page(url)
	#print content
	#print type(urlcontent) <type 'str'>
	hjson = json.loads(urlcontent)
	#print hjson
	#print "hjson['item_list'][1]['res_type']: ",hjson['item_list'][1]['res_type']
	#print type(hjson)  <type 'dict'>
	for item2 in hjson:
		#print "item2: " ,item2 
		#print "hjson[item2]: ",hjson[item2] 
		print  "type(hjson[item2]):", type(hjson[item2])





	print "txt file"
	position = "/Users/chenyating/Documents/Project/PyTrain/file/cookie.txt"
	cookieResult = "/Users/chenyating/Documents/Project/PyTrain/file/cookieResult.txt"
	writefile = file(cookieResult,'w')

	filecontent = get_file(position)
	#print filecontent
	#print type(filecontent) <type 'str'>
	fjson = json.loads(filecontent)
	#print fjson[0]['domain']
	#print type(fjson) <type 'list'>
	i=0
	for item in fjson:
		i=i+1
		print i
		#writefile.write(str(i)+'\n')  
		jxmDict={}
		#print "item",item 
		#print "type(item):",type(item)  # <type 'dict'>
		for itemlist in item:
			#writefile.write(str(itemlist) +": "+ str(item[itemlist])+'\n')
        	#print "item[",itemlist,"]",item[itemlist]
        	#print "type(itemlist):",type(itemlist) #<type 'unicode'>
			#print u" 参数名：", itemlist,u" 参数值：", item[itemlist]
			
		
			if (str(itemlist) =="name"):
				jxmDict['name'] = str(item[itemlist])
		
			elif(str(itemlist) =="value"):
				jxmDict['value'] = str(item[itemlist])
			elif(str(itemlist) =="domain"):
				jxmDict['domain'] = str(item[itemlist] )

			else:
				a=1

		print jxmDict
		writefile.write('''<elementProp name="'''+str(jxmDict["name"])+'''"  elementType="Cookie" "testname="'''+str(jxmDict["name"])+'">'+'\n')		
		writefile.write("	<stringProp name="+'"Cookie.value'+'">'+str(jxmDict["value"])+"</stringProp>"+'\n')
		writefile.write("	<stringProp name="+'"Cookie.value'+'">'+str(jxmDict["domain"])+"</stringProp>"+'\n')
		writefile.write('''	<stringProp name="Cookie.path"></stringProp>'''+'\n')
		writefile.write('''	<boolProp name="Cookie.secure">false</boolProp>'''+'\n')
		writefile.write('''	<longProp name="Cookie.expires">0</longProp>'''+'\n')
		writefile.write('''	<boolProp name="Cookie.path_specified">true</boolProp>'''+'\n')
		writefile.write('''	<boolProp name="Cookie.domain_specified">true</boolProp>'''+'\n')
		writefile.write('''</elementProp>'''+'\n')













if __name__=="__main__":
	main()