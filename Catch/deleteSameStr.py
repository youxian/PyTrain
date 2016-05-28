#!/usr/bin/python  
# coding:utf-8   

import sys
 
ReadFile = file(r"pingfen.txt","r")  
WriteFile = file(r"test1.txt","w+")  

a=[]
b=[]

for line in  ReadFile:
	a.append(line)
ReadFile.close()

for n in a: #遍历a中每一项（记为n），即1.txt中每一行
    flag=1
    for i in range(0,len(b)):
        if n == b[i][0]: #n与列表b中的每一项对比，如果有相等的：
            b[i][1]=b[i][1]+1 #那么对应的出现计数加1
            flag=0
            break
    if flag==1: #如果前面的比对没有一个相等的，即该行是第一次出现：
        b.append([n,1]) #那么在列表b中添加改行为新的一项
 
for n in b: #输出格式为：行信息 （tab） 出现次数 （回车）
    WriteFile.write(str(n[0][0:-1]) + "\t")
    WriteFile.write("\n") 
   # WriteFile.write(str(n[1]) + "\n") 
WriteFile.close