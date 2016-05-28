#-*- coding: UTF-8 -*-
#!/usr/bin/python

import re
import urllib 


writeFile =  file(r"xuanhuan.txt","w+")
for i in range(130):

	url="http://kansha.cc/shujilist.aspx?w_type=xuanhuan"+"&w_page="+str(i)
	#print url
	s=urllib.urlopen(url).read()
	urls=re.findall(r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')",s,re.I)
	no = 0 
	w="/shujitit.aspx?"
	for j in urls: 
		no = no+1  
		k =1
		if re.match(w,j)!=None:
			url3 = "http://kansha.cc"+j
			print url3
			writeFile.writelines(url3)
			writeFile.write("\n")


#<a href="/shujitit.aspx?w_nameno=69458" class="v4 black18" target="_blank">黄帝内经-灵枢 </a>
#http://kansha.cc/shujitit.aspx?w_nameno=64056