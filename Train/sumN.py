#-*- coding:utf-8 -*-
 
def sumN(n): 
	if (n%2 ==0):
		sum=(1+n)*(n/2)
		print "sum:",sum
	elif(n%2 ==1):
		sum = n*(n/2)+n
		print "sum:",sum
	else:
		print u"请输入正常的数字"

def sumN1(n):
	i=0
	sum1=0
	for i in range(0,n+1):
		sum1=sum1+i
	print sum1



# print  u"请输入最大数字" 
# n=input() 
# sumN(n)
